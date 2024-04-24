from dcelery.celery_config import app
import logging
from celery import Task, group
# IN Canvas designing workflow of documentation then groups 
"""
from dcelery.celery_tasks.ex4_error_handling_groups import run_tasks
"""


@app.task(queue='tasks')
def my_tt1(number):
    if number == 3:
        raise ValueError('Error number is invalid')
    return number * 2

def handle_result(result):
    if result.successful():
        print(f'Task completed successfully with {result.get()}')
    elif result.failed() and isinstance(result.result, ValueError):
        print(f'Task Failed {result.result}')
    elif result.status == 'REVOKED':
        print(f'Task was revoked by the worker{result.id }')
 

def run_tasks():
    task_group = group(my_tt1.s(i) for i in range(5))
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)

    for result in result_group:
        handle_result(result)