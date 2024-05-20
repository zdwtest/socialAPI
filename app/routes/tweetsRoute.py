# /app/routes/tweetsRoute.py
from flask import request, json, Blueprint, make_response, jsonify
from app.services.tweets import TweetService  # 导入 Service 类
from app.secure.jwtRequired import jwt_required
tweetRoute = Blueprint('tweetRoute', __name__)

tweet_service = TweetService()  # 实例化 Service


@tweetRoute.route('/tweets', methods=['GET'])
def get_tweets():
    """获取 Tweet 表中未被删除或隐藏的 ID 后 10 位内容、标签和其他内容"""

    # 获取请求参数
    tag = request.args.get('tag')
    user_id = request.args.get('user_id')
    tweet_id = request.args.get('tweet_id')
    cursor = request.args.get('cursor')  # 获取游标参数

    # 使用 Service 处理数据
    results, next_cursor = tweet_service.get_tweets(
        tag=tag, user_id=user_id, tweet_id=tweet_id, cursor=cursor, per_page=10
    )

    # 编码转换
    results_json = json.dumps(results, ensure_ascii=False)

    # 添加 next_cursor 到响应头
    response = make_response(results_json, 200, {'Content-Type': 'application/json; charset=utf-8'})
    if next_cursor:
        response.headers['X-Next-Cursor'] = next_cursor
    return response


@tweetRoute.route('/tweetsput', methods=['POST'])
def put_tweets():
    """更新推文"""
    # 获取推文 ID
    tweet_id = request.args.get('tweet_id')
    # 获取推文内容
    content = request.json.get('content')
    # 使用 Service 处理数据
    result = tweet_service.put_tweets(tweet_id, content)
    # 返回结果
    return result


@tweetRoute.route('/tweetscreate', methods=['POST'])
@jwt_required
def create_tweets():
    """创建推文"""

    # 从 cookie 获取用户 ID
    user_id = request.cookies.get('user_id')
    print(user_id)
    # 获取请求数据
    data_origin = request.get_json() # 获取 JSON 数据
    data = data_origin.copy()  # 避免修改原始数据
    data.update({'user_id': user_id})
    # 如果用户 ID 不存在，返回错误信息
    if not user_id:
        return jsonify({'success': False, 'message': '用户未登录'}), 401

    # 使用 Service 处理数据，将 user_id 传递给 create_tweet 方法
    result = tweet_service.create_tweet(data)
    # 返回状态
    return jsonify({'success': True, 'message': '推文创建成功','status':200})

# 使用示例 GET 方法
# GET /tweets HTTP/1.1 第一次访问
# GET /tweets?cursor=100 HTTP/1.1 第二次访问
