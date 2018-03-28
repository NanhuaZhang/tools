from celery_first_try import add, test_mes
import time
import sys


def pm(body):
    res = body.get('result')
    if body.get('status') == 'PROGRESS':
        sys.stdout.write('\r任务进度：{0}%'.format(res.get('p')))
        sys.stdout.flush()
    else:
        print('\r')
        print(res)


r = test_mes.delay()
print(r.get(on_message=pm, propagate=False))
# result = add.delay(4, 4)
# while not result.ready():
#     time.sleep(1)
# print('task done: {0}'.format(result.get()))
