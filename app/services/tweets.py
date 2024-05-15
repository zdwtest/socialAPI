from flask import Flask, jsonify, request

from app.database.models import Tweet, User

app = Flask(__name__)
@app.route('/tweets')
def get_tweets():
    tweets = Tweet.select().order_by(Tweet.created_at.desc())
    return jsonify([
        {
            'id': tweet.id,
            'user': tweet.user.username,
            'content': tweet.content,
            'tag': tweet.tag,
            'like': tweet.like,
            'view': tweet.view,
            'created_at': tweet.created_at.isoformat()  # 将 datetime 格式化为 ISO 8601 格式
        } for tweet in tweets
    ])

@app.route('/tweets', methods=['POST'])
def create_tweet():
    data = request.get_json()
    user = User.get_or_none(User.username == data['kalijerry'])
    if not user:
        return jsonify({'error': '用户不存在'}), 400
    tweet = Tweet.create(
        user=user,
        content=data['content'],
        tag=data['tag']
    )
    return jsonify({
        'id': tweet.id,
        'user': tweet.user.username,
        'content': tweet.content,
        'tag': tweet.tag,
        'like': tweet.like,
        'view': tweet.view,
        'created_at': tweet.created_at.isoformat()  # 将 datetime 格式化为 ISO 8601 格式
    }), 201

@app.route('/tweets/<int:tweet_id>')
def get_tweet(tweet_id):
    tweet = Tweet.get_or_none(Tweet.id == tweet_id)
    if not tweet:
        return jsonify({'error': '推文不存在'}), 404
    return jsonify({
        'id': tweet.id,
        'user': tweet.user.username,
        'content': tweet.content,
        'tag': tweet.tag,
        'like': tweet.like,
        'view': tweet.view,
        'created_at': tweet.created_at.isoformat()  # 将 datetime 格式化为 ISO 8601 格式
    })

@app.route('/tweets/<int:tweet_id>', methods=['PUT'])
def update_tweet(tweet_id):
    data = request.get_json()
    tweet = Tweet.get_or_none(Tweet.id == tweet_id)
    if not tweet:
        return jsonify({'error': '推文不存在'}), 404
    tweet.content = data.get('content', tweet.content)
    tweet.tag = data.get('tag', tweet.tag)
    tweet.save()
    return jsonify({
        'id': tweet.id,
        'user': tweet.user.username,
        'content': tweet.content,
        'tag': tweet.tag,
        'like': tweet.like,
        'view': tweet.view,
        'created_at': tweet.created_at.isoformat()  # 将 datetime 格式化为 ISO 8601 格式
    })

@app.route('/tweets/<int:tweet_id>', methods=['DELETE'])
def delete_tweet(tweet_id):
    tweet = Tweet.get_or_none(Tweet.id == tweet_id)
    if not tweet:
        return jsonify({'error': '推文不存在'}), 404
    tweet.delete_instance()
    return jsonify({'message': '推文已删除'}), 204

if __name__ == '__main__':
    app.run(debug=True)