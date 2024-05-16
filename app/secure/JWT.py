import jwt
import datetime

from jwt import ExpiredSignatureError, InvalidTokenError

from config import Config

# 示例密钥（用于签名和验证）
config = Config()
SECRET_KEY = config.SECRET_KEY


# 生成JWT
def create_jwt(data, key):
    # 构造头部
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }
    # 构造载荷
    payload = {
        "data": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 1小时后过期
    }
    # 生成JWT
    token = jwt.encode(payload, key, algorithm="HS256", headers=header)
    return token


def create_expiredJWT(data, key):
    # 构造头部
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }
    # 构造载荷
    payload = {
        "data": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=0)
    }
    # 生成JWT
    token = jwt.encode(payload, key, algorithm="HS256", headers=header)
    return token


# 验证JWT
def verify_jwt(token):
    try:
        # 解码 JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except ExpiredSignatureError:
        # Token 过期
        raise ExpiredSignatureError("Token has expired")
    except InvalidTokenError:
        # Token 无效
        raise InvalidTokenError("Invalid token")
