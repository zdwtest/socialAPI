import hashlib
from app.database.models import User


def login(username, password):
    """登录验证"""
    try:
        # 检查用户名是否存在
        user = User.get_or_none(User.username == username)
        if user:
            # 验证密码
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user.password == hashed_password:
                return True, "登录成功！"
            else:
                return False, "密码错误！"
        else:
            return False, "用户不存在！"
    except Exception as e:
        print(f"登录失败: {e}")
        return False, "登录失败，请重试！"


"""
# 测试登录
if __name__ == "__main__":
    # 用户输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 进行登录验证
    login(username, password)

"""
