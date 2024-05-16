import hashlib
from app.database.models import User

def register(username, password, email, age=None):
    """用户注册"""
    try:
        # 检查用户名是否已经存在
        existing_user = User.get_or_none(User.username == username)
        if existing_user:
            return False, "用户名已经存在，请选择其他用户名！"

        # 检查邮箱是否已经存在
        existing_email = User.get_or_none(User.email == email)
        if existing_email:
            return False, "邮箱地址已经存在，请选择其他邮箱地址！"

        # 将密码进行哈希处理
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 创建新用户
        new_user = User(
            username=username,
            password=hashed_password,
            email=email,
            age=age
        )

        # 保存新用户到数据库
        new_user.save()

        return True, "注册成功！"
    except Exception as e:
        print(f"注册失败: {e}")
        return False, "注册失败，请重试！"

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