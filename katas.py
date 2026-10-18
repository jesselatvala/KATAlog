import db

def get_katas(query=""):
    if query:
        sql = """SELECT katas.id, katas.title, users.username
                 FROM katas JOIN users ON katas.user_id = users.id
                 WHERE katas.title LIKE ? OR katas.description LIKE ?
                 ORDER BY katas.id DESC"""
        search = "%" + query + "%"
        return db.query(sql, [search, search])
    sql = """SELECT katas.id, katas.title, users.username
             FROM katas JOIN users ON katas.user_id = users.id
             ORDER BY katas.id DESC"""
    return db.query(sql)

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