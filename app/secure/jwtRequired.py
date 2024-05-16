from functools import wraps
from flask import request, jsonify
from jwt import ExpiredSignatureError, InvalidTokenError

from app.secure.JWT import verify_jwt


def jwt_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # Step 1: 获取在 cookie 中的 auth_token
        auth_token = request.cookies.get('auth_token')

        if not auth_token:
            return jsonify({'message': 'No auth token'}), 401

        else:
            try:
                # Step 2: 验证 auth_token
                verify_jwt(auth_token)
            except ExpiredSignatureError:
                # Token 过期
                return jsonify({'message': 'Token has expired'}), 401
            except InvalidTokenError:
                # Token 无效
                return jsonify({'message': 'Invalid token'}), 401

        # Step 3: 验证成功后放行函数
        return func(*args, **kwargs)

    return decorated_function
