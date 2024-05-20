# /app/services/tweets.py
from datetime import datetime

from flask import jsonify

from app.database.models import Tweet


class TweetService:
    def get_tweets(self, tag=None, user_id=None, tweet_id=None, cursor=None, per_page=10):
        """根据不同的参数查询 Tweet 表并进行分页"""

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

        # 使用游标分页
        if cursor:
            query = query.where(Tweet.id < cursor)

        # 限制查询数量
        tweets = [
            {
                'id': tweet.id,
                'content': tweet.content or '',
                'created_at': datetime.fromisoformat(tweet.created_at).isoformat(),
                'user': tweet.user.username,
                'tag': tweet.tag.split(',') if tweet.tag else [],
            }
            for tweet in query.order_by(Tweet.id.desc()).limit(per_page)
        ]

        # 返回结果和新的游标
        return tweets, tweets[-1]['id'] if tweets else None

    def put_tweets(self, tweet_id, content):
        """更新推文内容。

        Args:
            tweet_id (str): 推文 ID。
            content (str): 新的推文内容。

        Returns:
            dict: 包含更新结果的字典。
                - success (bool): 更新是否成功。
                - message (str): 更新结果信息。
        """

        # 检查推文是否存在
        tweet = self.get_tweet(tweet_id)  # 使用 get_tweet 获取单个推文
        if not tweet:
            return {'success': False, 'message': '推文不存在'}

        # 更新推文内容
        tweet.content = content  # 使用属性赋值更新 content

        # 将更新后的推文保存到数据库
        tweet.save()  # 使用 save() 方法保存

        return {'success': True, 'message': '推文更新成功'}

    def get_tweet(self, tweet_id):
        """获取单个推文"""
        try:
            tweet = Tweet.get(Tweet.id == tweet_id)
            return tweet
        except Tweet.DoesNotExist:
            return None

    def create_tweet(self, data):
        """创建新的推文。

        Args:
            data (dict): 包含推文信息的 JSON 数据。

        Returns:
            dict: 包含创建的推文信息的字典。
        """
        tweet = Tweet.create(
            user=data['user_id'],
            content=data['content'],
            title=data['title'],
            tag=data['tag']
        )

        return {'success': True, 'message': '推文创建成功'}
