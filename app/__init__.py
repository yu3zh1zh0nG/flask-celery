from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.celery_task import BaseTask



flask_app = Flask(__name__)
db = SQLAlchemy()
celery_app = Celery(
    flask_app.import_name,
    backend='redis://localhost:6379',
    broker='redis://localhost:6379'
)

def create_app():

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/db?charset=utf8'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    celery_app.conf.update(flask_app.config)
    class ContextTask(celery_app.Task, BaseTask):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)
    celery_app.Task = ContextTask

    print('init')
    db.init_app(flask_app)
    from app.views import a_bp
    from app.views import b_bp
    flask_app.register_blueprint(a_bp, url_prefix='/a')
    flask_app.register_blueprint(b_bp, url_prefix='/b')
    return flask_app




@flask_app.route('/')
def hello_world():
    return 'Hello World!'
