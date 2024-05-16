import os
import sqlite3
from contextlib import closing


def connect_database(database_name='mydb.db'):
    """连接到SQLite3数据库"""
    current_dir = os.path.dirname(__file__)  # 获取当前文件所在的目录路径
    parent_dir = os.path.dirname(current_dir)
    grandparent_dir = os.path.dirname(parent_dir)
    great_grandparent_dir = os.path.dirname(grandparent_dir)

    database_path = os.path.join(great_grandparent_dir, database_name)
    print(database_path)
    try:
        conn = sqlite3.connect(database_path)
        return conn
    except sqlite3.OperationalError as e:
        print(f"无法连接到数据库：{e}")
        return None


def execute_query(conn, query):
    """执行SQL查询并返回结果"""
    with closing(conn.cursor()) as cur:
        cur.execute(query)
        return cur.fetchall()


# 测试示例
if __name__ == "__main__":
    conn = connect_database()
    if conn is not None:
        rows = execute_query(conn, "SELECT * FROM User")
        for row in rows:
            print(row)
        conn.close()
