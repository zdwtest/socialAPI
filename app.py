from flask import Flask
from app.routes.likeRoute import likeRoute
from app.routes.tweetsRoute import tweetRoute
from app.routes.replyRoute import replyRoute
from app.routes.viewRoute import viewRoute
from app.routes.loginRoute import loginRoute
from app.routes.registerRoute import registerRoute

app = Flask(__name__)

app.register_blueprint(likeRoute)
app.register_blueprint(tweetRoute)
app.register_blueprint(replyRoute)
app.register_blueprint(viewRoute)
app.register_blueprint(loginRoute)
app.register_blueprint(registerRoute)


if __name__ == '__main__':
    app.run()
