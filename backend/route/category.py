import os
import sqlite3
from flask import Blueprint, jsonify, json

category_bp = Blueprint("category", __name__)

# 配置JSON不使用ASCII编码 (支持中文返回)
category_bp.json_provider_class = lambda: json.JSONProvider(
    ensure_ascii=False, sort_keys=False
)


@category_bp.route("/category")
def get_categories():
    # 获取项目根目录路径（route目录的上级目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_root, "database", "chino.db")

    if not os.path.exists(db_path):
        return jsonify({"error": "数据库文件不存在"}), 500

    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # 让结果可以通过列名访问
        cursor = conn.cursor()

        # 查询所有分类的 id, name, route
        cursor.execute("SELECT id, name, route FROM chino_category")
        categories = cursor.fetchall()

        conn.close()

        # 将 row 对象转换为字典列表
        result = []
        for row in categories:
            result.append({"id": row["id"], "name": row["name"], "route": row["route"]})

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@category_bp.route("/<category_route>/article")
def get_articles_by_category(category_route):
    # ... (前置代码不变) ...
    # 获取项目根目录路径
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_root, "database", "chino.db")

    if not os.path.exists(db_path):
        return jsonify({"error": "数据库文件不存在"}), 500
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        db_route = f"/category/{category_route}"

        # 修改：SELECT 中增加 a.cover
        query = """
            SELECT 
                a.id, 
                a.title, 
                a.description, 
                a.create_time, 
                a.update_time,
                a.cover
            FROM chino_article a
            JOIN chino_category c ON a.category_id = c.id
            WHERE c.route = ?
            ORDER BY a.id DESC
        """

        cursor.execute(query, (db_route,))
        articles = cursor.fetchall()
        conn.close()

        result = []
        for row in articles:
            # 修改：返回字典中增加 cover
            result.append(
                {
                    "id": row["id"],
                    "title": row["title"],
                    "description": row["description"],
                    "create_time": row["create_time"],
                    "update_time": row["update_time"],
                    "cover": row["cover"],  # 新增
                }
            )

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
