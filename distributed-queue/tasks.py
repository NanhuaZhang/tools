from celery.utils.log import get_task_logger
from celery import Celery

app = Celery('celery_first_try', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.__dict__)
    return x + y