# /app/services/reply.py
from datetime import datetime
from app.database.models import Reply

class ReplyService:
    def get_replies(self, tweet_id=None, user_id=None):
        """根据不同的参数查询 Reply 表"""

        query = Reply.select(
            Reply.id,
            Reply.content,
            Reply.created_at,
            Reply.user,
            Reply.tweet
        ).where(
            Reply.is_deleted == False,
            Reply.is_blocked == False
        )

        # 添加查询条件
        if tweet_id:
            query = query.where(Reply.tweet_id == tweet_id)
        if user_id:
            query = query.where(Reply.user_id == user_id)

        # 限制查询数量
        query = query.limit(100)

        # 执行查询并构建结果
        results = []
        for reply in query:
            # 构建结果字典
            result = {
                'id': reply.id,
                'content': reply.content or '',
                'created_at': datetime.fromisoformat(reply.created_at).isoformat(),
                'user': reply.user.username,
                'tweet_id': reply.tweet.id
            }

            results.append(result)

        return results

    def create_reply(self, data):
        """创建新的回复"""

        reply = Reply.create(
            user=data['user_id'],
            content=data['content'],
            tweet=data['tweet_id']
        )

        return {'success': True, 'message': '回复创建成功'}