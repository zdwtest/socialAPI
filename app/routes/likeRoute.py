# /app/routes/likesRoute.py
from flask import Flask, jsonify, request, json, Blueprint

from app.secure.jwtRequired import jwt_required
from app.services.like import LikeService  # 导入 Service 类

likeRoute = Blueprint('likeRoute', __name__)

like_service = LikeService()  # 实例化 Service


@likeRoute.route('/likes/tweet/<int:tweet_id>', methods=['POST'])
@jwt_required
def like_tweet_route(tweet_id):
    """点赞推文"""
    result, status_code = like_service.like_tweet(tweet_id)
    return jsonify(result), status_code


@likeRoute.route('/likes/reply/<int:reply_id>', methods=['POST'])
@jwt_required
def like_reply_route(reply_id):
    """点赞评论"""
    result = like_service.like_reply(reply_id)
    return jsonify(result), 200


