import hashlib
from app.database.db import connect_database


def login(username, password):
    """登录验证"""
    # 连接到数据库
    conn = connect_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=?", (username,))
    user = cur.fetchone()

    if user:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user[2] == hashed_password:
            cur.close()
            conn.close()
            return True, "登录成功！"
        else:
            cur.close()
            conn.close()
            return False, "密码错误！"
    else:
        cur.close()
        conn.close()
        return False, "用户不存在！"


"""
# 测试登录
if __name__ == "__main__":
    # 连接到数据库
    conn = connect_database('../mydb.db')

    # 用户输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 进行登录验证
    login(conn, username, password)


"""
