# /app/routes/replyRoute.py
from flask import request, json, Blueprint, jsonify
from app.services.reply import ReplyService  # 导入 Service 类
from app.secure.jwtRequired import jwt_required

replyRoute = Blueprint('replyRoute', __name__)

reply_service = ReplyService()  # 实例化 Service

@replyRoute.route('/replies', methods=['GET'])
def get_replies():
    """获取 Reply 表中未被删除或屏蔽的评论内容"""

    # 获取请求参数
    tweet_id = request.args.get('tweet_id')
    user_id = request.args.get('user_id')

    # 使用 Service 处理数据
    results = reply_service.get_replies(tweet_id, user_id)

    # 编码转换
    results_json = json.dumps(results, ensure_ascii=False)

    return jsonify({'success': True, 'replies': results}), 200

@replyRoute.route('/repliescreate', methods=['POST'])
@jwt_required
def create_reply():
    """创建新的回复"""

    # 从 cookie 获取用户 ID
    user_id = request.cookies.get('user_id')

    # 获取请求数据
    data_origin = request.get_json()
    data = data_origin.copy()
    data.update({'user_id': user_id})

    # 如果用户 ID 不存在，返回错误信息
    if not user_id:
        return jsonify({'success': False, 'message': '用户未登录'}), 401

    # 使用 Service 处理数据，将 user_id 传递给 create_reply 方法
    result = reply_service.create_reply(data)

    # 返回状态
    return jsonify({'success': True, 'message': '回复创建成功'}), 200

# 使用示例 GET 方法
# /replies?tweet_id=1
# /replies?user_id=1

# 使用示例 POST 方法
# POST /replies HTTP/1.1
# Content-Type: application/json
# {
#   "tweet_id": 1,
#   "content": "This is a reply."
# }