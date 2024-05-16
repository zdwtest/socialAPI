import random
import time

from flask import Flask, request, jsonify, json, session, make_response
from app.services.login import login
from app.services.cookie import set_cookies
from config import Config

app = Flask(__name__)

config = Config()


@app.route('/login', methods=['POST', 'GET'])
def login_route():
    if request.method == 'GET':
        # 处理GET请求，例如提供登录页面（如果是API，可以省略）
        response = {"message": "请通过POST请求提交用户名和密码进行登录"}
        return app.response_class(
            response=json.dumps(response, ensure_ascii=False),
            mimetype='application/json'
        )

    elif request.method == 'POST':
        # 获取JSON格式的请求数据
        # JSON格式为{"username": "username1", "password": "password1"}
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # 检查参数
        if not username or not password:
            return jsonify({"success": False, "message": "用户名和密码不能为空"}), 400

        # 调用登录函数验证用户
        success, message = login(username, password)
        response = {"success": success, "message": message}

        # 生成 session_id
        timestamp = int(time.time())
        random_part = random.randint(1000, 9999)
        session_id = f"{timestamp}_{random_part}"
        # 获取 cookie 数据
        cookie_data = set_cookies(username, session_id)
        auth_token = cookie_data['auth_token']
        encrypted_user_id = cookie_data['encrypted_user_id']
        encrypted_session_id = cookie_data['encrypted_session_id']
        encrypted_user_prefs = cookie_data['encrypted_user_prefs']

        # 设置 cookie
        resp = make_response(json.dumps(response, ensure_ascii=False), 200 if success else 401)
        resp.mimetype = 'application/json'
        resp.set_cookie('user_id', encrypted_user_id, httponly=True, samesite='Strict', max_age=3600)
        resp.set_cookie('session_id', encrypted_session_id, httponly=True, samesite='Strict', max_age=3600)
        resp.set_cookie('user_prefs', encrypted_user_prefs, httponly=True, samesite='Strict', max_age=3600)
        resp.set_cookie('auth_token', auth_token, httponly=True, samesite='Strict', max_age=3600)

        return resp


if __name__ == '__main__':
    app.run(debug=True)
