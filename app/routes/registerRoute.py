from flask import request, jsonify, json, Blueprint
from app.services.register import register

registerRoute = Blueprint('registerRoute', __name__)

@registerRoute.route('/register', methods=['POST', 'GET'])
def register_route():
    if request.method == 'GET':
        # 处理GET请求，例如提供登录页面（如果是API，可以省略）
        response = {"message": "请通过POST请求提交用户名和密码进行注册"}
        return json.dumps(response, ensure_ascii=False), 200, {'Content-Type': 'application/json'}

    elif request.method == 'POST':
        # 获取JSON格式的请求数据
        # JSON格式为{"username": "username", "password": "password","email":"email"}
        data = request.json
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        age = data.get('age')

        # 检查参数
        if not username or not password:
            return jsonify({"success": False, "message": "用户名和密码不能为空"}), 400

        # 调用注册函数
        success, message = register(username, password, email, age)
        response = {"success": success, "message": message}
        return json.dumps(response, ensure_ascii=False), 200 if success else 401, {'Content-Type': 'application/json'}


