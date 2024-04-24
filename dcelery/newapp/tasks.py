from celery import shared_task
import time

# @shared_task(task_rate_limit = '1/m')
# def t1(queue = 'celery'):
#     time.sleep(3)
#     return


@shared_task
def t1(queue = 'celery'):
    time.sleep(3)
    return

@shared_task
def t2(queue = 'celery:1'):
    time.sleep(3)
    return

@shared_task
def t3(queue = 'celery:2'):
    time.sleep(3)
    return

@shared_task
def t4(queue = 'celery:3'):
    time.sleep(3)  
    return

  