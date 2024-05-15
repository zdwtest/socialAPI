from app.database.models import Tweet, Reply, User

# 测试用例1：创建用户、推文和回复

# 假设要使用的用户 ID 为 1
user_id = 1

# 从数据库获取用户对象
user = User.get(User.id == user_id)
def test_create_user_tweet_reply():
    # 创建用户
    #user = User.create(username='test_user', password='password', email='test@example.com', age=25)
    assert user.id is not None  # 检查用户ID是否生成

    # 创建推文
    tweet = Tweet.create(user=user, content='这是一个测试推文', tag='test')
    assert tweet.id is not None  # 检查推文ID是否生成

    # 创建回复
    reply = Reply.create(user=user, tweet=tweet, content='这是一条回复')
    assert reply.id is not None  # 检查回复ID是否生成

    # 检查关联关系
    assert tweet.user == user
    assert reply.tweet == tweet
    assert reply.user == user

# 测试用例2：获取推文的回复

def test_get_tweet_replies():
    # 创建一个测试推文
    #user = User.create(username='test_user', password='password', email='test@example.com', age=25)
    tweet = Tweet.create(user=user, content='这是一个测试推文', tag='test')

    # 创建两个回复
    Reply.create(user=user, tweet=tweet, content='回复1')
    Reply.create(user=user, tweet=tweet, content='回复2')

    # 获取推文的所有回复
    replies = tweet.replies

    # 检查回复数量
    assert len(replies) == 2

    # 检查回复内容
    for reply in replies:
        assert reply.content in ['回复1', '回复2']

# 测试用例3：获取用户的推文

def test_get_user_tweets():
    # 创建一个测试用户
    #user = User.create(username='test_user', password='password', email='test@example.com', age=25)

    # 创建两个推文
    Tweet.create(user=user, content='推文1', tag='test')
    Tweet.create(user=user, content='推文2', tag='test')

    # 获取用户的推文
    tweets = user.tweets

    # 检查推文数量
    assert len(tweets) == 2

    # 检查推文内容
    for tweet in tweets:
        assert tweet.content in ['推文1', '推文2']

# 测试用例4：删除推文和回复

def test_delete_tweet_and_replies():
    # 创建一个测试用户
    #user = User.create(username='test_user', password='password', email='test@example.com', age=25)

    # 创建一个测试推文和回复
    tweet = Tweet.create(user=user, content='这是一个测试推文', tag='test')
    reply = Reply.create(user=user, tweet=tweet, content='这是一条回复')

    # 删除推文
    tweet.delete_instance()

    # 检查推文是否删除
    assert Tweet.get_or_none(id=tweet.id) is None

    # 检查回复是否被级联删除
    assert Reply.get_or_none(id=reply.id) is None

# 测试用例5：更新推文内容

def test_update_tweet_content():
    # 创建一个测试用户
    #user = User.create(username='test_user', password='password', email='test@example.com', age=25)

    # 创建一个测试推文
    tweet = Tweet.create(user=user, content='这是一个测试推文', tag='test')

    # 更新推文内容
    tweet.content = '更新后的推文内容'
    tweet.save()

    # 检查推文内容是否更新
    assert tweet.content == '更新后的推文内容'

# 测试用例6：添加标签

def test_add_tag_to_tweet():
    # 创建一个测试用户
    #user = User.create(username='test_user', password='password', email='test@example.com', age=25)

    # 创建一个测试推文
    tweet = Tweet.create(user=user, content='这是一个测试推文', tag='test')

    # 添加一个新的标签
    new_tag = 'new_tag'
    tweet.tags.add(new_tag)

    # 检查推文是否添加了新的标签
    assert new_tag in tweet.tags.names()

def get_user_tweets(user_id):
    """获取指定用户的所有推文"""
    user = User.get(User.id == user_id)
    tweets = user.tweets
    return tweets
def print_user_tweets(user_id):
    tweets = get_user_tweets(user_id)
    for tweet in tweets:
        print(tweet.content)

def insert_tweet(user_id):
    user = User.get(User.id == user_id)
    Tweet.create(user=user_id,content="我在测试1", tag='test')

def reply_tweet(tweet_id):
    Reply.create(user=user_id,content="很好的发帖1", tweet=tweet_id, tag='test')

def print_tweet_replies(tweet_id):
    """打印指定推文的回复"""
    tweet = Tweet.get(Tweet.id == tweet_id)
    replies = tweet.replies
    for reply in replies:
        print(f"回复 ID: {reply.id}, 内容: {reply.content}")
# 运行测试用例
if __name__ == '__main__':
    #test_create_user_tweet_reply()
    #test_get_tweet_replies()
    #test_get_user_tweets()
    #test_delete_tweet_and_replies()
    #test_update_tweet_content()
    #test_add_tag_to_tweet()
    #insert_tweet(1) #用户id为1
    #print_user_tweets(1)

    #reply_tweet(2) #帖子id为2
    print_tweet_replies(2) #帖子id为2


    print("所有测试用例通过！")