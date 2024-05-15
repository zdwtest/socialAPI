from flask import Flask, make_response, request, redirect
from app.JWT import create_jwt, verify_jwt, create_expiredJWT
from app.encrypt import encrypt_data, decrypt_data
from config import Config

config = Config()  # 初始化配置
app = Flask(__name__)

# 引入密钥并进行编码
SECRET_KEY_origin = config.SECRET_KEY  # 引入原始的密钥
SECRET_KEY = SECRET_KEY_origin.encode('utf-8')  # 进行编码


@app.route('/verify')  # 测试
def verify():
    auth_token = request.cookies.get('auth_token')
    return verify_jwt(auth_token, SECRET_KEY_origin)


@app.route('/expired')  # 测试jwt过期情况
def expired():
    data = {"session_id": "abcde12345",
            "user_id": "12345"}
    auth_token = create_expiredJWT(data, SECRET_KEY)

    resp = make_response("Cookies have been set!")
    resp.set_cookie('auth_token', auth_token)
    return resp


def set_cookies(user_id, session_id, user_prefs='none'):
    # 创建 JWT
    auth_token = create_jwt({"user_id": user_id, "session_id": session_id}, SECRET_KEY_origin)

    # 加密敏感数据
    encrypted_user_id = encrypt_data(user_id, SECRET_KEY)
    encrypted_session_id = encrypt_data(session_id, SECRET_KEY)
    encrypted_user_prefs = encrypt_data(user_prefs, SECRET_KEY)

    # 创建字典
    cookie_data = {
        'auth_token': auth_token,
        'encrypted_user_id': encrypted_user_id,
        'encrypted_session_id': encrypted_session_id,
        'encrypted_user_prefs': encrypted_user_prefs
    }

    return cookie_data




@app.route('/getcookies')  # 测试使用
def get_cookies():
    encrypted_user_id = request.cookies.get('userid')
    encrypted_session_id = request.cookies.get('session_id')
    encrypted_user_prefs = request.cookies.get('user_prefs')
    auth_token = request.cookies.get('auth_token')
    if encrypted_user_id and encrypted_session_id and encrypted_user_prefs:
        try:
            user_id = decrypt_data(encrypted_user_id, SECRET_KEY)
            session_id = decrypt_data(encrypted_session_id, SECRET_KEY)
            user_prefs = decrypt_data(encrypted_user_prefs, SECRET_KEY)
            return (f'User ID: {user_id}, Session ID: {session_id},'
                    f' User Preferences: {user_prefs},Auth Token:{auth_token}')
        except Exception as e:
            return f'Error decrypting cookies: {e}'
    return 'No cookies found!'


if __name__ == "__main__":
    app.run(debug=True)
