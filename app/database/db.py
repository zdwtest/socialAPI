import os
import sqlite3


def connect_database(database_name='mydb.db'):
    """连接到SQLite3数据库"""
    current_dir = os.path.dirname(__file__)  # 获取当前文件所在的目录路径

    # 获取上上级目录
    parent_dir = os.path.dirname(current_dir)
    grandparent_dir = os.path.dirname(parent_dir)
    great_grandparent_dir = os.path.dirname(grandparent_dir)

    database_path = os.path.join(great_grandparent_dir, database_name)
    conn = sqlite3.connect(database_path)
    return conn


def execute_query(conn, query):
    """执行SQL查询并返回结果"""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows
