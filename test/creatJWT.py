from flask import Flask, make_response,  jsonify

from app.secure.JWT import create_expiredJWT,create_jwt

app=Flask(__name__)
@app.route('/expiredJWT')
def test():
    # 创建一个过期的 JWT
    token = create_expiredJWT('123', '123')

    # 创建响应对象
    response = make_response(jsonify({'message': 'OK'}))

    # 将 JWT 写入到 cookie 中
    response.set_cookie('auth_token', token)

    return response
@app.route('/jwt')
def jwt():
    # 创建一个 JWT
    token = create_jwt('123','123')
    # 创建响应对象
    response = make_response(jsonify({'message': 'OK'}))
    # 将 JWT 写入到 cookie 中
    response.set_cookie('auth_token', token)
    return response

if __name__ == '__main__':
    app.run(debug=True)
