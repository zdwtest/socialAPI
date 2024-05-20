import json
import requests
def test_create_tweets():
    """测试创建推文的路由"""

    # 测试数据
    test_data = {
        'user': 1,  # 替换为实际的用户 ID
        'content': '这是一条测试推文',
        'title': '测试推文标题',
        'tag': 'test,python',
    }

    # 发送 POST 请求
    response = requests.post('http://127.0.0.1:5000/tweetscreate', json=test_data)  # 替换为你的服务器地址和端口

    # 断言响应状态码为 200
    assert response.status_code == 200

    # 解析响应数据
    response_data = response.json()

    # 断言响应数据中包含 success 和 message 字段
    assert 'success' in response_data
    assert 'message' in response_data

    # 断言创建成功
    assert response_data['success'] is True
    assert response_data['message'] == '推文创建成功'

    # 可以根据需要添加更多断言，例如检查创建的推文是否包含正确的字段等