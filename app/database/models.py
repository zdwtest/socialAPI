from datetime import datetime, timezone, timedelta

from app import db  # 从 app/__init__.py 中导入数据库实例

from peewee import CharField, IntegerField, ForeignKeyField, TextField, DateTimeField, AutoField, BooleanField

utc_now = datetime.now(timezone.utc)
now = bj_dt = utc_now.astimezone(timezone(timedelta(hours=8)))


# 创建时区UTC+8:00，即东八区对应的时区


class User(db.Model):
    """用户模型"""
    username = CharField(unique=True)  # 用户名，唯一
    password = CharField()  # 密码哈希值
    email = CharField(unique=True)  # 邮箱，唯一
    age = IntegerField(null=True)  # 年龄，可以为空
    is_deleted = BooleanField(default=False)  # 是否删除，默认为 False
    is_blocked = BooleanField(default=False)  # 是否屏蔽，默认为 False


class Tweet(db.Model):
    """推文模型"""
    user = ForeignKeyField(User, backref='tweets')  # 关联用户模型，反向关系为 'tweets'
    content = TextField()  # 推文内容
    like = IntegerField(default=0)
    view = IntegerField(default=0)
    tag = TextField(default="default")  # 标签，存储以逗号分隔的标签字符串
    created_at = DateTimeField(default=now)  # 创建时间
    is_deleted = BooleanField(default=False)  # 是否删除，默认为 False


class Reply(db.Model):
    """评论模型"""
    user = ForeignKeyField(User, backref='replies')  # 关联用户模型，反向关系为 'replies'
    tweet = ForeignKeyField(Tweet, backref='replies')  # 关联推文模型，反向关系为 'replies'
    content = TextField()
    created_at = DateTimeField(default=now)  # 创建时间
    like = IntegerField(default=0)
    view = IntegerField(default=0)
    is_deleted = BooleanField(default=False)  # 是否删除，默认为 False
    is_blocked = BooleanField(default=False)  # 是否屏蔽，默认为 False


# 创建数据库表
db.create_tables([User, Tweet, Reply])
