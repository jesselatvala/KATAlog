import db

def get_katas(query="", style=""):
    sql = """SELECT katas.id, katas.title, users.username
             FROM katas JOIN users ON katas.user_id = users.id
             WHERE (katas.title LIKE ?
                    OR katas.description LIKE ?
                    OR katas.developer LIKE ?)"""
    search = "%" + query + "%"
    params = [search, search, search]
    if style:
        sql += " AND katas.style = ?"
        params.append(style)
    sql += " ORDER BY katas.id DESC"
    return db.query(sql, params)

def get_kata(kata_id):
    sql = """SELECT katas.id, katas.title, katas.description,
                    katas.developer, katas.style, katas.techniques,
                    katas.user_id, users.username
             FROM katas JOIN users ON katas.user_id = users.id
             WHERE katas.id = ?"""
    result = db.query(sql, [kata_id])
    return result[0] if result else None

def add_kata(title, description, user_id, developer, style, techniques):
    sql = """INSERT INTO katas (title, description, user_id, developer, style, techniques)
             VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, description, user_id, developer, style, techniques])
    return db.last_insert_id()

def update_kata(kata_id, title, description, user_id, developer, style, techniques):
    sql = """UPDATE katas SET title = ?, description = ?, developer = ?,
             style = ?, techniques = ? WHERE id = ? AND user_id = ?"""
    db.execute(sql, [title, description, developer, style, techniques, kata_id, user_id])

def remove_kata(kata_id, user_id):
    sql = "DELETE FROM katas WHERE id = ? AND user_id = ?"
    db.execute(sql, [kata_id, user_id])

def get_statistics():
    sql = "SELECT COUNT(*) AS total FROM users"
    user_total = db.query(sql)[0]["total"]

    sql = "SELECT COUNT(*) AS total FROM katas"
    kata_total = db.query(sql)[0]["total"]

    sql = """SELECT COUNT(DISTINCT LOWER(TRIM(developer))) AS total FROM katas WHERE TRIM(developer) != ''"""
    developer_total = db.query(sql)[0]["total"]

    sql = """SELECT COUNT(DISTINCT LOWER(TRIM(style))) AS total
             FROM katas
             WHERE TRIM(style) != ''"""
    style_total = db.query(sql)[0]["total"]

    sql = "SELECT techniques FROM katas"
    all_katas = db.query(sql)
    longest_kata = 0
    for kata in all_katas:
        technique_count = 0
        for line in kata["techniques"].splitlines():
            if line.strip():
                technique_count += 1
        if technique_count > longest_kata:
            longest_kata = technique_count

    return {
        "user_total": user_total,
        "kata_total": kata_total,
        "developer_total": developer_total,
        "style_total": style_total,
        "longest_kata": longest_kata
    }