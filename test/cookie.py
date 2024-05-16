from flask import Flask, request, jsonify
from app.services.cookie import get_deCookies , get_cookies


app = Flask(__name__)


@app.route('/get_cookies')
def get_cookies_route():
    response = jsonify(get_cookies(request))
    return response

@app.route('/get_decookies')
def get_decookies_route():
    user_id = get_deCookies(request)['user_id']
    print(user_id)
    response = jsonify(get_deCookies(request))
    return response

if __name__ == "__main__":
    app.run(debug=True)
