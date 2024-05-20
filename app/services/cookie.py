from app.secure.JWT import create_jwt
from app.secure.encrypt import encrypt_data, decrypt_data
from config import Config

config = Config()  # 初始化配置

# 引入密钥并进行编码
SECRET_KEY_origin = config.SECRET_KEY  # 引入原始的密钥
SECRET_KEY = SECRET_KEY_origin.encode('utf-8')  # 进行编码


def set_cookies(user,username, uuid, session_id, user_prefs):
    # 创建 JWT
    auth_token = create_jwt({"user_id": uuid, "session_id": session_id}, SECRET_KEY_origin)

    # 加密敏感数据
    encrypted_username = encrypt_data(username, SECRET_KEY)
    encrypted_uuid = encrypt_data(uuid, SECRET_KEY)
    encrypted_session_id = encrypt_data(session_id, SECRET_KEY)
    encrypted_user_prefs = encrypt_data(user_prefs, SECRET_KEY)

    # 创建字典
    cookie_data = {
        'user_id': user,
        'auth_token': auth_token,
        'encrypted_username': encrypted_username,
        'encrypted_user_id': encrypted_uuid,
        'encrypted_session_id': encrypted_session_id,
        'encrypted_user_prefs': encrypted_user_prefs
    }

    return cookie_data


# 获取解密后的Cookies
def get_deCookies(request):
    user_id = request.cookies.get('user_id')
    encrypted_user_id = request.cookies.get('uuid')
    encrypted_session_id = request.cookies.get('session_id')
    encrypted_user_prefs = request.cookies.get('user_prefs')
    auth_token = request.cookies.get('auth_token')
    # 解密Cookie内容
    uuid = decrypt_data(encrypted_user_id, SECRET_KEY)
    session_id = decrypt_data(encrypted_session_id, SECRET_KEY)
    user_prefs = decrypt_data(encrypted_user_prefs, SECRET_KEY)
    # 将多个变量封装成 JSON 对象
    response_data = {
        'user_id':user_id,
        'uuid': uuid,
        'session_id': session_id,
        'user_prefs': user_prefs,
        'auth_token': auth_token
    }
    return response_data


# 获取未解密的Cookies
def get_cookies(request):
    encrypted_user_id = request.cookies.get('user_id')
    encrypted_session_id = request.cookies.get('session_id')
    encrypted_user_prefs = request.cookies.get('user_prefs')
    auth_token = request.cookies.get('auth_token')
    # 将多个变量封装成 JSON 对象
    response_data = {
        'encrypted_user_id': encrypted_user_id,
        'encrypted_session_id': encrypted_session_id,
        'encrypted_user_prefs': encrypted_user_prefs,
        'auth_token': auth_token
    }
    return response_data
