from dcelery.celery_config import app
import logging
from celery import Task
"""
from dcelery.celery_tasks.ex3_auto_retry import my_tt
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

@app.task(queue='tasks', autoretry_for=(ConnectionError,), default_retry_delay=5, max_retries=5)
def my_tt():
    raise ConnectionError('EX3 connection error ........')
    return
