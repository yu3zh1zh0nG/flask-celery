from flask import Blueprint, current_app
from app.models import Article, db
from app.tasks import add
a_bp=Blueprint('aName',__name__)
from app import flask_app, create_app
@a_bp.route('/')
def index():
    print(flask_app)
    # print(create_app())
    print(current_app)
    print(id(flask_app))
    # print(id(create_app()))
    print(id(current_app))
    print(db)
    result = add.delay(23, 42)
    # print(result.get())
    return 'response'