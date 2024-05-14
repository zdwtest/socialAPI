from app.models import User, Tweet

# 创建用户
#user = User.create(username='john1', password='secret', email='john1@example.com', age=30)

# 创建推文
tweet = Tweet.create(user_id="john1", content='Hello, world! TEST1',tag="test",like="0",view="0")
