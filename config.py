import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件


class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY')  # 密钥，用于加密 cookie
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app/mydb.db'  # 数据库 URI


class DevelopmentConfig(Config):
    """开发环境配置类"""
    DEBUG = True  # 启用调试模式


class TestingConfig(Config):
    """测试环境配置类"""
    TESTING = True  # 启用测试模式
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 使用内存数据库


class ProductionConfig(Config):
    """生产环境配置类"""
    DEBUG = False  # 禁用调试模式
    # ... 其他生产环境配置 ...
