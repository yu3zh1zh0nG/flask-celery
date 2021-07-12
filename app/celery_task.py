import celery
from celery import Celery


class BaseTask(celery.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    # 任务成功时执行
    def on_success(self, retval, task_id, args, kwargs):
        from app import flask_app
        from app.models import Article,db
        print('***')
        with flask_app.app_context():
            art = Article(title='test', content='zzzzz')
            db.session.add(art)
            db.session.commit()
            print(Article.query.all())
        print(retval)
        print(task_id)
        print(args)
        print(kwargs)

    # 任务重试时执行
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass
