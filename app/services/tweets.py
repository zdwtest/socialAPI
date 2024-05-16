#/app/services/tweets.py
from datetime import datetime

from app.database.models import  Tweet


class TweetService:
    def get_tweets(self, tag=None, user_id=None, tweet_id=None):
        """根据不同的参数查询 Tweet 表"""

        query = Tweet.select(
            Tweet.id,
            Tweet.content,  # 获取完整的 content
            Tweet.created_at,
            Tweet.user,
            Tweet.tag,
        ).where(
            Tweet.is_deleted == False
        )

        # 添加查询条件
        if tag:
            query = query.where(Tweet.tag.contains(tag))
        if user_id:
            query = query.where(Tweet.user_id == user_id)
        if tweet_id:
            query = query.where(Tweet.id == tweet_id)

        # 限制查询数量
        query = query.limit(100)

        # 执行查询并构建结果
        results = []
        for tweet in query:
            # 获取标签名称
            tag_names = tweet.tag.split(',') if tweet.tag else []

            # 构建结果字典
            result = {
                'id': tweet.id,
                'content': tweet.content or '',  # 修正条件判断
                'created_at': datetime.fromisoformat(tweet.created_at).isoformat(),  # 将字符串转换为 datetime 对象
                'user': tweet.user.username,
                'tag': tag_names,
            }

            results.append(result)

        return results