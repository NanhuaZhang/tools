from celery import Celery

# tasks.py
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
app.config_from_object('celery_config')


@app.task(bind=True)
def period_task(self):
    print('period task done: {0}'.format(self.request.id))



