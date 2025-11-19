import os
import sqlite3
from flask import Blueprint, jsonify, json

article_bp = Blueprint("article", __name__)

# 配置JSON不使用ASCII编码
article_bp.json_provider_class = lambda: json.JSONProvider(
    ensure_ascii=False, sort_keys=False
)


def get_db_connection():
    """获取数据库连接"""
    conn = sqlite3.connect("database/chino.db")
    conn.row_factory = sqlite3.Row
    return conn


@article_bp.route("/article/<int:article_id>")
def get_article(article_id):
    # 获取项目根目录路径（route目录的上级目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 检查markdown文件是否存在
    md_file_path = os.path.join(project_root, "articles", f"{article_id}.md")
    print(md_file_path)

    if not os.path.exists(md_file_path):
        return jsonify({"error": "文章文件不存在"}), 404

    try:
        # 读取markdown文件内容
        with open(md_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 数据库路径也需要使用绝对路径
        db_path = os.path.join(project_root, "database", "chino.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        # 查询当前文章信息
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT a.id, a.title, a.description, a.create_time, a.update_time, c.name as category
            FROM chino_article a
            LEFT JOIN chino_category c ON a.category_id = c.id
            WHERE a.id = ?
        """,
            (article_id,),
        )

        current_article = cursor.fetchone()

        # 如果数据库中没有文章信息，使用默认值
        if not current_article:
            current_article = {
                "id": article_id,
                "title": None,
                "category": None,
                "description": None,
                "create_time": None,
                "update_time": None,
            }
            prev_article = None
            next_article = None
        else:
            # 查询同分类的上一篇文章
            cursor.execute(
                """
                SELECT a.id, a.title, a.description, a.create_time, a.update_time
                FROM chino_article a
                WHERE a.category_id = (SELECT category_id FROM chino_article WHERE id = ?)
                AND a.id < ?
                ORDER BY a.id DESC
                LIMIT 1
            """,
                (article_id, article_id),
            )

            prev_article = cursor.fetchone()

            # 查询同分类的下一篇文章
            cursor.execute(
                """
                SELECT a.id, a.title, a.description, a.create_time, a.update_time
                FROM chino_article a
                WHERE a.category_id = (SELECT category_id FROM chino_article WHERE id = ?)
                AND a.id > ?
                ORDER BY a.id ASC
                LIMIT 1
            """,
                (article_id, article_id),
            )

            next_article = cursor.fetchone()

        conn.close()

        # 构建返回数据
        response = {
            "id": current_article["id"],
            "title": current_article["title"],
            "category": current_article["category"],
            "description": current_article["description"],
            "create_time": current_article["create_time"],
            "update_time": current_article["update_time"],
            "content": content,
            "previous": {
                "id": prev_article["id"] if prev_article else None,
                "title": prev_article["title"] if prev_article else None,
                "description": prev_article["description"] if prev_article else None,
                "create_time": prev_article["create_time"] if prev_article else None,
                "update_time": prev_article["update_time"] if prev_article else None,
            },
            "next": {
                "id": next_article["id"] if next_article else None,
                "title": next_article["title"] if next_article else None,
                "description": next_article["description"] if next_article else None,
                "create_time": next_article["create_time"] if next_article else None,
                "update_time": next_article["update_time"] if next_article else None,
            },
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@article_bp.route("/articles", methods=["GET"])
def get_all_articles():
    """返回所有文章元数据列表"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_root, "database", "chino.db")
    if not os.path.exists(db_path):
        return jsonify({"error": "数据库文件不存在"}), 500
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT a.id, a.title, a.description, a.cover, a.create_time, a.update_time, c.name as category
            FROM chino_article a
            LEFT JOIN chino_category c ON a.category_id = c.id
            ORDER BY a.id DESC
            """
        )
        articles = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return jsonify(articles)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
