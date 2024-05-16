from flask import Flask, jsonify, request, json
from app.services.tweets import TweetService  # 导入 Service 类

app = Flask(__name__)

tweet_service = TweetService()  # 实例化 Service


@app.route('/tweets', methods=['GET'])
def get_tweets():
    """获取 Tweet 表中未被删除或隐藏的 ID 后 10 位内容、标签和其他内容"""

    # 获取请求参数
    tag = request.args.get('tag')
    user_id = request.args.get('user_id')
    tweet_id = request.args.get('tweet_id')

    # 使用 Service 处理数据
    results = tweet_service.get_tweets(tag, user_id, tweet_id)

    # 编码转换
    results_json = json.dumps(results, ensure_ascii=False)

    return results_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run(debug=True)

# 使用示例 GET 方法
# /tweets?tweet_id=1
# /tweets?tag=default
# /tweets?user_id=1