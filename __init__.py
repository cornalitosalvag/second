import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
            SECRET_KEY='mikey',
            DATABASE_HOST=os.environ.get('ble5mmo2o5v9oouq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'),
            DATABASE_PASSWORD=os.environ.get('tqkb217eerv38ddo'),
            DATABASE_USER=os.environ.get('u4jofa5m2zaocsu7'),
            DATABASE=os.environ.get('ir5mplk9rirjxupk'),
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'pichuletincito'

    return app


