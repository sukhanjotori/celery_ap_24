from dcelery.celery_config import app
import logging
from celery import Task
"""
from dcelery.celery_tasks.ex_name_custom import my_task
"""
# to save into log file
logging.basicConfig(filename='app.log', level=logging.ERROR, format=f'%(asctime)s - %(levelname)s - %(message)s')

# custom class
class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("Connection Error - Admin Notified", exc_info=True)
        else:
            print(f'{0!r} failed{1!r}'.format(task_id, exc))

        
app.Task = CustomTask

@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError('connection error occured...')
    except ConnectionError: 
        raise ConnectionError()

