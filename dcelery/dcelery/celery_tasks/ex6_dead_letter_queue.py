from dcelery.celery_config import app
import logging
from celery import Task, group, chain
# IN Canvas designing workflow of documentation then groups 
"""
from dcelery.celery_tasks.ex6_dead_letter_queue import run_group
"""
# TODO: Get latest code of this file from zip file
app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True

@app.task(queue='tasks')
def my_task(z):
    try:
        if z==2:
            raise ValueError('Wrong number error')
    except Exception as e:
        handle_failed_task.apply_async(args=(z,str(e))) # send exception to failed task handler
        # raise  # if you still want to send it to failure task then uncomment this line. (it will appear both in failure and succeed tasks.)

@app.task(queue='dead_letter')
def handle_failed_task(z, exception): 
    return 'custom logic to process'


def run_group():
    task_group = group(
        my_task.s(1),
        my_task.s(2),
        my_task.s(3),
    )
    task_group.apply_async()
    # task_group.get()