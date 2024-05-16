#/app/services/likes.py
from flask import jsonify

from app.database.models import Tweet, Reply, User

class LikeService:
    def like_tweet(self, tweet_id):
        """点赞推文"""
        tweet = Tweet.get_by_id(tweet_id)
        tweet.like += 1
        tweet.save()
        return {'message': '点赞成功'}

    def like_reply(self, reply_id):
        """点赞评论"""
        reply = Reply.get_by_id(reply_id)
        reply.like += 1
        reply.save()
        return {'message': '点赞成功'}