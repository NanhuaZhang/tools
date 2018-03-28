import gevent.monkey as monkey
from celery import Celery
monkey.patch_all()

app = Celery('asyncResult', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y
# celery -A tasks worker --loglevel=info


def on_result_ready(result):
    print('Received result for id %r: %r' % (result.id, result.result,))


add.delay(2, 2).then(on_result_ready)