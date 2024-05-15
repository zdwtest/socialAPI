import sqlite3


def connect_database():
    """连接到SQLite3数据库"""
    conn = sqlite3.connect('/app/mydb.db')
    return conn


def execute_query(conn, query):
    """执行SQL查询并返回结果"""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows
