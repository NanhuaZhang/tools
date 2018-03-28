# from celery import Celery, Task
#
# app = Celery('celery_first_try', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
#
#
# class MyTask(Task):
#     def on_success(self, retval, task_id, args, kwargs):
#         print('su task done: {0}'.format(retval))
#         return super(MyTask, self).on_success(retval, task_id, args, kwargs)
#
#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         print('fa task done: {0}'.format(exc))
#         return super(MyTask, self).on_success(exc, task_id, args, kwargs)
#
#
# @app.task
# def add(x, y):
#     return x+y
#
from celery.utils.log import get_task_logger
from celery import Celery

app = Celery('celery_first_try', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.__dict__)
    return x + y