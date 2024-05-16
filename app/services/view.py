# /app/services/view.py
from app.database.models import Tweet, Reply


class ViewService:
    def view_tweet(self, tweet_id):
        """查看推文"""
        tweet = Tweet.get_by_id(tweet_id)
        tweet.view += 1
        tweet.save()
        return {'message': '推文查看成功'}

    def view_reply(self, reply_id):
        """查看评论"""
        reply = Reply.get_by_id(reply_id)
        reply.view += 1
        reply.save()
        return {'message': '评论查看成功'}
