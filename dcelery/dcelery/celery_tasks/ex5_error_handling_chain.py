from dcelery.celery_config import app
import logging
from celery import Task, group, chain
# IN Canvas designing workflow of documentation then groups 
"""
from dcelery.celery_tasks.ex5_error_handling_chain import run_chain
"""


@app.task(queue='tasks')
def add(x,y):
    return x + y


@app.task(queue='tasks')
def multiply(z):
    if z==8:
        raise ValueError('Zero not accepted')
    return z * 2


def run_chain():
    task_chain = chain(add.s(4, 4), multiply.s())
    result = task_chain.apply_async()
    result.get() # propag
