import hashlib
from app.database.db import connect_database


def register(username, password, email, age=None):
    """用户注册"""
    # 连接到数据库
    conn = connect_database()
    cur = conn.cursor()

    try:
        # 检查用户名是否已经存在
        cur.execute("SELECT * FROM User WHERE username=?", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            return False, "用户名已经存在，请选择其他用户名！"

        # 将密码进行哈希处理
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 插入新用户到数据库
        cur.execute("INSERT INTO User (username, password, email, age) VALUES (?, ?, ?, ?)",
                    (username, hashed_password, email, age))
        conn.commit()
        return True, "注册成功！"
    finally:
        # 关闭游标和连接
        cur.close()
        conn.close()


"""
#测试注册
if __name__ == "__main__":
    # 用户输入注册信息
    username = input("请输入用户名：")
    password = input("请输入密码：")
    email = input("请输入邮箱：")
    age = input("请输入年龄（可选）：")

    # 进行注册
    register(username, password, email, age)
"""
