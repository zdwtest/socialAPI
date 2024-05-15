from flask import Flask, make_response, request
import hashlib
from app.db import connect_database


def register(username, password, email, age=None):
    """用户注册"""
    # 连接到数据库
    conn = connect_database()

    # 检查用户名是否已经存在
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=?", (username,))
    existing_user = cur.fetchone()
    if existing_user:
        print("用户名已经存在，请选择其他用户名！")
        return

    # 将密码进行哈希处理
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # 插入新用户到数据库
    cur.execute("INSERT INTO user (username, password, email, age) VALUES (?, ?, ?, ?)",
                (username, hashed_password, email, age))
    conn.commit()
    print("注册成功！")

    # 关闭数据库连接
    cur.close()
    conn.close()


if __name__ == "__main__":
    # 用户输入注册信息
    username = input("请输入用户名：")
    password = input("请输入密码：")
    email = input("请输入邮箱：")
    age = input("请输入年龄（可选）：")

    # 进行注册
    register(username, password, email, age)
