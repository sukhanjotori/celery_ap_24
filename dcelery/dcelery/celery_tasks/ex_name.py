from dcelery.celery_config import app
import logging
"""
from dcelery.celery_tasks.ex_name import my_task
"""
# to save into log file
logging.basicConfig(filename='app.log', level=logging.ERROR, format=f'%(asctime)s - %(levelname)s - %(message)s')


@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError('connectio error occured...')
    except ConnectionError: 
        logging.error("Connection Error", exc_info=True)
        raise ConnectionError()

