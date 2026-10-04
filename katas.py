import db


def get_katas():
    sql = """SELECT katas.id, katas.title, users.username
             FROM katas JOIN users ON katas.user_id = users.id
             ORDER BY katas.id DESC"""
    return db.query(sql)
