#/app/routes/viewsRoute.py
from flask import Flask, jsonify, request, json
from app.services.view import ViewService  # 导入 Service 类

app = Flask(__name__)

view_service = ViewService()  # 实例化 Service

@app.route('/views/tweet/<int:tweet_id>', methods=['POST'])
def view_tweet(tweet_id):
    """查看推文"""
    result = view_service.view_tweet(tweet_id)
    return jsonify(result), 200

@app.route('/views/reply/<int:reply_id>', methods=['POST'])
def view_reply(reply_id):
    """查看评论"""
    result = view_service.view_reply(reply_id)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
