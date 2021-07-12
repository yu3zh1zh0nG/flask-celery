from flask import current_app
from app import celery_app
from app.models import Article


@celery_app.task()
def add(x,y):
    print('=====')
    print(Article.query.all())
    return x+y