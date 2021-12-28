import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
            SECRET_KEY='mikey',
            DATABASE_HOST='ble5mmo2o5v9oouq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            DATABASE_PASSWORD='tqkb217eerv38ddo',
            DATABASE_USER='u4jofa5m2zaocsu7',
            DATABASE='ir5mplk9rirjxupk',
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


