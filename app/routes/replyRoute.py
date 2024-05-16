#/app/routes/replyRoute.py
from flask import Flask, jsonify, request, json
from app.services.reply import ReplyService  # 导入 Service 类

app = Flask(__name__)

reply_service = ReplyService()  # 实例化 Service

@app.route('/replies', methods=['GET'])
def get_replies():
    """获取 Reply 表中未被删除或屏蔽的评论内容"""

    # 获取请求参数
    tweet_id = request.args.get('tweet_id')
    user_id = request.args.get('user_id')

    # 使用 Service 处理数据
    results = reply_service.get_replies(tweet_id, user_id)

    # 编码转换
    results_json = json.dumps(results, ensure_ascii=False)

    return results_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run(debug=True)

# 使用示例 GET 方法
# /replies?tweet_id=1
# /replies?user_id=1