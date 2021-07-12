from flask import Blueprint,current_app
b_bp=Blueprint('bName',__name__)
from app import  flask_app, create_app
@b_bp.route('/')
def index():
    print(flask_app)
    print(create_app())
    print(current_app)
    print(id(flask_app))
    print(id(create_app()))
    print(id(current_app))
    return 'response'