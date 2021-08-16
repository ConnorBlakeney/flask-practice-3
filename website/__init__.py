from flask import Flask

def create_app(self):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'howdy'

    return app
