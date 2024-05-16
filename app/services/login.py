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

def get_user_id(username):
    user_id = User.get_or_none(User.username == username)
    if user_id:
        return User.id
    else:
        return None

username = "kalijerry"
user_id = get_user_id(username)

if user_id:
    print(f"用户 '{username}' 的 ID 为 {user_id}")
else:
    print(f"用户 '{username}' 不存在")


