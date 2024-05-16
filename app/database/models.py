# 数据库模型
from datetime import datetime, timezone, timedelta

from app import db  # 从 app/__init__.py 中导入数据库实例

from peewee import CharField, IntegerField, ForeignKeyField, TextField, DateTimeField, AutoField, ManyToManyField, \
    BooleanField

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
class Tag(db.Model):
    """标签模型"""
    name = CharField(unique=True)


class Tweet(db.Model):
    """推文模型"""
    user = ForeignKeyField(User, backref='tweets')  # 关联用户模型，反向关系为 'tweets'
    content = TextField()  # 推文内容
    tags = ManyToManyField(Tag, backref='tweets')  # 关联标签模型
    created_at = DateTimeField(default=now)  # 创建时间
    is_deleted = BooleanField(default=False)  # 是否删除，默认为 False

class TweetTag(db.Model):
    """推文和标签的关联表"""
    tweet = ForeignKeyField(Tweet)
    tag = ForeignKeyField(Tag)


class Reply(db.Model):
    """评论模型"""
    user = ForeignKeyField(User, backref='replies')  # 关联用户模型，反向关系为 'replies'
    tweet = ForeignKeyField(Tweet, backref='replies')  # 关联推文模型，反向关系为 'replies'
    content = TextField()
    created_at = DateTimeField(default=now)  # 创建时间
    is_deleted = BooleanField(default=False)  # 是否删除，默认为 False
    is_blocked = BooleanField(default=False)  # 是否屏蔽，默认为 False

# 创建数据库表
db.create_tables([User, Tweet, Tag, TweetTag, Reply])
