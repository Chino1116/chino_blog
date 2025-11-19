import os
import sqlite3
from flask import Flask
from route.article import article_bp
from route.category import category_bp
from route.admin import admin_bp  # 导入 admin 蓝图
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)


def init_directories():
    directories = ["database", "articles", "route"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"创建目录: {directory}")


# --- 核心修改开始 ---


def get_target_schema():
    """定义期望的数据库结构"""
    return {
        "chino_category": {
            "columns": {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "name": "TEXT NOT NULL UNIQUE",
                "route": "TEXT",
            },
            "constraints": [],
        },
        "chino_article": {
            "columns": {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "category_id": "INTEGER",
                "title": "TEXT NOT NULL",
                "description": "TEXT",
                "cover": "TEXT",  # 确保包含 cover 字段
                "create_time": "TEXT",
                "update_time": "TEXT",
            },
            "constraints": ["FOREIGN KEY (category_id) REFERENCES chino_category (id)"],
        },
    }


def sync_table(cursor, table_name, schema):
    """同步单个表的结构：检查字段，若不一致则重建表"""

    # 1. 检查表是否存在
    cursor.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    )
    if not cursor.fetchone():
        print(f"[{table_name}] 表不存在，正在创建...")
        create_table(cursor, table_name, schema)
        return

    # 2. 获取当前表的所有字段名
    cursor.execute(f"PRAGMA table_info({table_name})")
    current_columns = {row[1] for row in cursor.fetchall()}
    target_columns = set(schema["columns"].keys())

    # 3. 比较字段：如果相等，则无需操作
    if current_columns == target_columns:
        print(f"[{table_name}] 结构正确，无需更新。")
        return

    # 4. 结构不一致，开始迁移（添加缺失，删除多余）
    print(f"[{table_name}] 结构不匹配。正在同步结构...")
    print(f"  - 当前字段: {current_columns}")
    print(f"  - 目标字段: {target_columns}")

    # 4.1 重命名旧表
    temp_table_name = f"{table_name}_backup_{os.urandom(4).hex()}"
    cursor.execute(f"ALTER TABLE {table_name} RENAME TO {temp_table_name}")

    # 4.2 创建新表（使用最新定义的结构）
    create_table(cursor, table_name, schema)

    # 4.3 计算新旧表的交集字段（只保留两边都有的字段数据）
    common_columns = list(current_columns.intersection(target_columns))

    if common_columns:
        columns_str = ", ".join(common_columns)
        print(f"  - 迁移保留字段: {columns_str}")
        # 将旧表数据复制到新表
        cursor.execute(
            f"""
            INSERT INTO {table_name} ({columns_str})
            SELECT {columns_str} FROM {temp_table_name}
        """
        )

    # 4.4 删除旧表
    cursor.execute(f"DROP TABLE {temp_table_name}")
    print(f"[{table_name}] 结构同步完成。")


def create_table(cursor, table_name, schema):
    """根据 Schema 生成 CREATE TABLE 语句并执行"""
    col_defs = []
    for col_name, col_type in schema["columns"].items():
        col_defs.append(f"{col_name} {col_type}")

    # 合并字段定义和约束
    full_defs = col_defs + schema["constraints"]
    sql = f"CREATE TABLE {table_name} ({', '.join(full_defs)})"
    cursor.execute(sql)


def init_database():
    """初始化并同步数据库"""
    db_path = "database/chino.db"

    # 连接数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 启用外键约束
    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        target_schema = get_target_schema()

        # 遍历定义好的 Schema 进行同步
        for table_name, schema in target_schema.items():
            sync_table(cursor, table_name, schema)

        conn.commit()
        print("数据库结构检查与同步完成")

    except Exception as e:
        print(f"数据库初始化出错: {e}")
        conn.rollback()
    finally:
        conn.close()


# --- 核心修改结束 ---


@app.route("/")
def index():
    return "Flask应用已启动，数据库和目录已初始化"


app.register_blueprint(article_bp)
app.register_blueprint(category_bp)
app.register_blueprint(admin_bp)  # 注册 admin 蓝图

if __name__ == "__main__":
    init_directories()
    init_database()
    app.run(host="localhost", port=8000, debug=True)
