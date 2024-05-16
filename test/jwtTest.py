from flask import jsonify, Flask

from app.secure.jwtRequired import jwt_required

app = Flask(__name__)


# 这是你的修饰器函数
def verify_token(token):
    # 这里是一个简单的示例，你需要根据你使用的 JWT 库来实现验证逻辑
    if token == "valid_token":
        return True
    else:
        return False


# 这是你的路由函数，应用了 jwt_required 修饰器
@app.route('/protected')
@jwt_required
def protected_route():
    message = 'OK'
    # 直接返回包含中文字符的 JSON 字典
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True)
