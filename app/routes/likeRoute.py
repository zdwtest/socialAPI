#/app/routes/likesRoute.py
from flask import Flask, jsonify, request, json
from app.services.like import LikeService  # 导入 Service 类

app = Flask(__name__)

like_service = LikeService()  # 实例化 Service

@app.route('/likes/tweet/<int:tweet_id>', methods=['POST'])
def like_tweet(tweet_id):
    """点赞推文"""
    result = like_service.like_tweet(tweet_id)
    return jsonify(result), 200

@app.route('/likes/reply/<int:reply_id>', methods=['POST'])
def like_reply(reply_id):
    """点赞评论"""
    result = like_service.like_reply(reply_id)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
