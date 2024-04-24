from dcelery.celery_config import app
import logging
from celery import Task, group, chain
from time import sleep
import sys
# IN Canvas designing workflow of documentation then groups 
"""
from dcelery.celery_tasks.ex8_linking_result_callbacks import run_task
run_task()

"""
# TODO: Get latest code of this file from zip file

@app.task(queue='tasks')
def long_running_task():
    raise ValueError('value error in task')

@app.task(queue='tasks')
def process_task_result(result):
    sys.stdout.write('process task result')
    sys.stdout.flush() 


@app.task(queue='tasks')
def error_handler(task_id, exc, traceback):
    sys.stdout.write('>>>>')
    sys.stdout.write(str(exc))
    sys.stdout.write('>>>>')
    sys.stdout.flush() 

def run_task():
    long_running_task.apply_async(link=[process_task_result.s(),], link_error=[error_handler.s(),])