from flask import Flask, make_response, request
import hashlib
from app.db import connect_database


def login(conn, username, password):
    """登录验证"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=?", (username,))
    user = cur.fetchone()
    if user:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user[2] == hashed_password:
            print("登录成功！")
        else:
            print("密码错误！")
    else:
        print("用户不存在！")
    cur.close()


if __name__ == "__main__":
    # 连接到数据库
    conn = connect_database()

    # 用户输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 进行登录验证
    login(conn, username, password)

    # 关闭数据库连接
    conn.close()
