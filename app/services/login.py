import hashlib

from flask import json

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

def get_uuid(username):
    # 查询username的uuid
    username_to_find = username
    query = User.select(User.uuid).where(User.username == username_to_find)

    try:
        user = query.get()
        # print(f"The UUID for user '{username_to_find}' is: {user.uuid}")
        # 将UUID转换为字符串
        uuid_str = str(user.uuid)
        # 将字符串序列化为JSON
        uuid = json.dumps({"uuid": uuid_str})
        return uuid
    except User.DoesNotExist:
        print(f"No user found with username '{username_to_find}'")
        return None  # 或者你可以选择返回一个默认值
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # 捕获其他可能的异常，并返回 None



