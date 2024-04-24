import os
from celery import Celery
# Set default config values.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
from kombu import Queue, Exchange
import time

app = Celery("dcelery")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = {
    Queue('tasks',Exchange('tasks'), routing_key = 'tasks', 
          queue_arguments = {'x-max-priority':10}),
    Queue('dead_letter', routing_key='dead_letter'),
}

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


base_dir = os.getcwd()
task_folder = os.path.join(base_dir, 'dcelery','celery_tasks')
if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith('ex') and filename.endswith('.py'):
            module_name = f'dcelery.celery_tasks.{filename[:-3]}'
            module = __import__(module_name, fromlist=['*'])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) : # and name.startswith('my_tasks'):
                    task_modules.append(f'{module_name}.{name}')



app.autodiscover_tasks(task_modules)



# @app.task(queue = 'tasks')
# def mq1(a, b, message = None):
#     time.sleep(3)
#     result = a + b 
#     if message:
#         result = f'{result}: {message}'
#     return result


# @app.task(queue = 'tasks')
# def mq2():
#     time.sleep(3)

# @app.task(queue = 'tasks')
# def mq3():
#     time.sleep(3)


# @app.task(queue = 'tasks')
# def mq4():
#     time.sleep(3)


# # for redis
# # app.conf.task_routes = {'newapp.tasks.task1':{'queue':'queue1'}, 'newapp.tasks.task2':{'queue':'queue2'}}

# # app.conf.task_default_rate_limit = '1/m'

# # app.conf.broker_transport_options = {
# #     'priority_steps': list(range(10)),
# #     'sep':':',
# #     'queue_order_strategy': 'priority'
# # }



# def test():
#     # Call the task asynchronously
#     result = mq1.apply_async(args=[5,13], kwargs={"message":"The sum is"})

#     # Check if the task has completed
#     if result.ready():
#         print("Task has completed")
#     else:
#         print("Task is still running")

#     # Check if the task completed successfully
#     if result.successful():
#         print("Task completed successfully")
#     else:
#         print("Task encountered an error")

#     # Get the result of the task
#     try:
#         task_result = result.get()
#         print("Task result:", task_result)
#     except Exception as e:
#         print("An exception occurred:", str(e))

#     # Get the exception (if any) that occurred during task execution
#     exception = result.get(propagate=False)
#     if exception:
#         print("An exception occurred during task execution:", str(exception))

# def exe_sync():
#     result = mq1.apply_async(args=[5,5], kwargs={'message':'Adding numbers'})
#     task_result = result.get()
#     print('This task is running synchronously')
#     print(task_result)

# def exe_async():
#     result = mq1.apply_async(args=[5,5], kwargs={'message':'Adding numbers'})
#     print('This task is running asynchronously')
#     print('Task id', result.task_id)
 


# @app.task
# def add_numbers():
#     return 

# Load task modules from all registered Django apps.

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


