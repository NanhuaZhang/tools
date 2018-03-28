from celery_first_try import add
import time

result = add.delay(4, 4)
while not result.ready():
    time.sleep(1)
print('task done: {0}'.format(result.get()))
