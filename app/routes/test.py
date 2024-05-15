from app.JWT import create_jwt
from config import Config

config = Config()  # 初始化配置

# 示例密钥（16字节的随机密钥）
SECRET_KEY_origin = config.SECRET_KEY  # 引入原始的密钥
SECRET_KEY = SECRET_KEY_origin.encode('utf-8')  # 进行编码

data = {"user_id": 12345, "username": "testuser"}


create_jwt(data,SECRET_KEY)
