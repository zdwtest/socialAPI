from flask import Flask
from peewee import SqliteDatabase, Model, CharField, IntegerField
from config  import Config

# 创建 Peewee 数据库实例
db = SqliteDatabase('mydb.db')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 其他 Flask 应用初始化...

    return app
