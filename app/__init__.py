import os
from flask import Flask
from peewee import SqliteDatabase, Model, CharField, IntegerField
from config import Config

# 获取项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(project_root, 'mydb.db')

# 使用绝对路径创建 Peewee 数据库实例
db = SqliteDatabase(database_path)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 其他 Flask 应用初始化...

    return app
