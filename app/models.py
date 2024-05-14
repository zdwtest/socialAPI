# 数据库模型
import datetime

from app import db  # 从 app/__init__.py 中导入数据库实例

from peewee import CharField, IntegerField, ForeignKeyField, TextField, DateTimeField, Model


class User(db.Model):
    """用户模型"""
    username = CharField(unique=True)  # 用户名，唯一
    password = CharField()  # 密码  此功能在测试完毕后用hash进行验证
    email = CharField(unique=True)  # 邮箱，唯一
    age = IntegerField(null=True)  # 年龄，可以为空


class Tweet(db.Model):
    """推文模型"""
    user = ForeignKeyField(User, backref='tweets')  # 关联用户模型，反向关系为 'tweets'
    content = TextField()  # 推文内容
    tag = TextField()  # 标签
    like = CharField()  # 点赞数
    view = CharField()  # 观看数
    created_at = DateTimeField(default=datetime.datetime.now)  # 创建时间


# 创建数据库表
db.create_tables([User, Tweet])
