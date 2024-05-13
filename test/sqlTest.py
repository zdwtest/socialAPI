from app.models import User, Tweet

# 创建用户
user = User.create(username='john1', password='secret', email='john1@example.com', age=30)

# 创建推文
tweet = Tweet.create(user=user, content='Hello, world!')