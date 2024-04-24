from dcelery.celery_config import app
import logging
from celery import Task, group, chain
from time import sleep
import sys
# IN Canvas designing workflow of documentation then groups 
"""
from dcelery.celery_tasks.ex7_task_timeouts_revoking import long_running_task
long_running_task.delay()
from dcelery.celery_tasks.ex7_task_timeouts_revoking import execute_task_examples
execute_task_examples()
"""
# TODO: Get latest code of this file from zip file

@app.task(queue='tasks',time_limit=10)
def long_running_task():
    sleep(6)
    return 'Task completed successfully'

@app.task(queue='task', bind=True)
def process_task_result(self,result):
    if result is None:
        return "Task was revoked, skipping result processing"
    else:
        return f'Task result: {result}'

def execute_task_examples():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=40)
    except TimeoutError:
        print('Task timed out')

    task = long_running_task.delay()
    task.revoke(terminate=True)
    # the revoke process takes some time to change the status of task from pending to revoked so simply put sleep(3)
    sys.stdout.write(task.status)

    if task.status =='REVOKED':
        process_task_result.delay(None)
    else:
        process_task_result.delay(task.status)
