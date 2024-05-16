from app.database.models import User, Tweet, Reply

# 创建一个新用户，默认未删除和未屏蔽
# user = User.create(username='test', password='password', email='john@example.com', age=30)
user = User.get(User.id == 1)  # 获取 ID 为 1 的用户

# 设置用户为删除状态
# user.is_deleted = True
# 保存更改到数据库
user.save()

# 创建一条推文，默认未删除
# tweet = Tweet.create(user=user, content='Hello world!')

tweet = Tweet.get(Tweet.id == 1)
# 设置推文为删除状态
# tweet.is_deleted = True
tweet.save()

# 获取被删除的用户
users_del = User.select().where(User.is_deleted == True)

# 遍历用户列表，获取每个用户的用户名
for User in users_del:
    print(User.username)

# 获取被删除的推文
tweets_del = Tweet.select().where(Tweet.is_deleted == True)

# 遍历推文列表
for Tweet in tweets_del:
    print(Tweet.id)

# 创建 Reply 实例并保存到数据库
reply = Reply.create(user=user, tweet=tweet, content="很好1")