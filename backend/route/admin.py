import os
import sqlite3
from flask import Blueprint, request, jsonify

admin_bp = Blueprint("admin", __name__)

# 后台密钥（建议后续可从环境变量或配置文件读取）
ADMIN_KEY = "Chino_Secret_1116"


def get_db_connection():
    conn = sqlite3.connect("database/chino.db")
    conn.row_factory = sqlite3.Row
    return conn


# 分类管理（仅查询无需鉴权）
@admin_bp.route("/api/admin/category", methods=["GET"])
def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, route FROM chino_category")
    categories = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(categories)


# 分类新增/编辑/删除（POST，需鉴权）
@admin_bp.route("/api/admin/category", methods=["POST"])
def category_post():
    data = request.json
    key = data.get("key")
    if key != ADMIN_KEY:
        return jsonify({"error": "无权限", "success": False}), 401
    action = data.get("action")
    conn = get_db_connection()
    cursor = conn.cursor()
    if action == "add":
        cursor.execute(
            "INSERT INTO chino_category (name, route) VALUES (?, ?)",
            (data["name"], data["route"]),
        )
        conn.commit()
        conn.close()
        return jsonify({"success": True, "msg": "分类新增成功"})
    elif action == "update":
        cursor.execute(
            "UPDATE chino_category SET name=?, route=? WHERE id=?",
            (data["name"], data["route"], data["id"]),
        )
        conn.commit()
        conn.close()
        return jsonify({"success": True, "msg": "分类修改成功"})
    elif action == "delete":
        cursor.execute("DELETE FROM chino_category WHERE id=?", (data["id"],))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "msg": "分类删除成功"})
    conn.close()
    return jsonify({"error": "未知操作", "success": False}), 400


# 文章管理（仅查询无需鉴权）
@admin_bp.route("/api/admin/article", methods=["GET"])
def get_articles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT a.id, a.title, a.description, a.cover, a.category_id, a.create_time, a.update_time, c.name as category_name FROM chino_article a LEFT JOIN chino_category c ON a.category_id = c.id"
    )
    articles = []
    for row in cursor.fetchall():
        art = dict(row)
        # 时间戳转格式化字符串
        for t in ["create_time", "update_time"]:
            ts = art.get(t)
            if ts:
                try:
                    ts_int = int(float(ts))
                    art[t] = time_format(ts_int)
                except Exception:
                    art[t] = ts
        articles.append(art)
    conn.close()
    return jsonify(articles)


def time_format(ts):
    import time

    return time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime(ts))


# 文章新增/编辑/删除（POST，需鉴权）
@admin_bp.route("/api/admin/article", methods=["POST"])
def article_post():
    data = request.json
    key = data.get("key")
    if key != ADMIN_KEY:
        return jsonify({"error": "无权限", "success": False}), 401
    action = data.get("action")
    conn = get_db_connection()
    cursor = conn.cursor()
    now_ts = int(__import__("time").time())
    if action == "add":
        cursor.execute(
            "INSERT INTO chino_article (title, description, cover, category_id, create_time, update_time) VALUES (?, ?, ?, ?, ?, ?)",
            (
                data["title"],
                data["description"],
                data["cover"],
                data["category_id"],
                now_ts,
                now_ts,
            ),
        )
        conn.commit()
        article_id = cursor.lastrowid
        if "markdown" in data:
            articles_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "articles"
            )
            os.makedirs(articles_dir, exist_ok=True)
            md_path = os.path.join(articles_dir, f"{article_id}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(data["markdown"])
        conn.close()
        return jsonify({"success": True, "msg": "文章新增成功"})
    elif action == "update":
        cursor.execute(
            "UPDATE chino_article SET title=?, description=?, cover=?, category_id=?, update_time=? WHERE id=?",
            (
                data["title"],
                data["description"],
                data["cover"],
                data["category_id"],
                now_ts,
                data["id"],
            ),
        )
        conn.commit()
        if "markdown" in data:
            articles_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "articles"
            )
            os.makedirs(articles_dir, exist_ok=True)
            md_path = os.path.join(articles_dir, f"{data['id']}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(data["markdown"])
        conn.close()
        return jsonify({"success": True, "msg": "文章修改成功"})
    elif action == "delete":
        cursor.execute("DELETE FROM chino_article WHERE id=?", (data["id"],))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "msg": "文章删除成功"})
    conn.close()
    return jsonify({"error": "未知操作", "success": False}), 400
