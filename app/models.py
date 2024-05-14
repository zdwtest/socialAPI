# 数据库模型
from datetime import datetime, timezone, timedelta

from app import db  # 从 app/__init__.py 中导入数据库实例

from peewee import CharField, IntegerField, ForeignKeyField, TextField, DateTimeField

utc_now = datetime.now(timezone.utc)
now = bj_dt = utc_now.astimezone(timezone(timedelta(hours=8)))


# 创建时区UTC+8:00，即东八区对应的时区


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
    created_at = DateTimeField(default=now)  # 创建时间


class Reply(db.Model):
    """评论模型"""
    user = ForeignKeyField(User, backref='replies')  # 关联用户模型，反向关系为 'replies'
    content = TextField()
    created_at = DateTimeField(default=now)  # 创建时间


# 创建数据库表
db.create_tables([User, Tweet, Reply])
