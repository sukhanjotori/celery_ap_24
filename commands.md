docker-compose up -d --build
chmod +x ./entrypoint.sh   
python manage.py startapp cworker



docker exec -it django /bin/sh
python manage.py shell
from newapp.tasks import sharedtask
sharedtask.delay()




task1.delay()
task3.delay()
task2.delay()
task4.delay()
task2.delay()
task3.delay()
task1.delay()
task4.delay()
task2.delay()
task1.delay()
task4.delay()
task3.delay()
task1.delay()

from dcelery.celery import mq1,mq2,mq3,mq4



pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh

# Run on Django to inspect task
celery inspect active
celery inspect active_queues

# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)

t1.delay()

from celery import group, chain
from newapp.tasks import t1, t2, t3, t4
task_group = group(t1.s(), t2.s(), t3.s(), t4.s())
task_group.apply_async()

from celery import group, chain
from newapp.tasks import t1, t2, t3, t4
task_chain = chain(t1.s(), t2.s(), t3.s())
task_chain.apply_async()

from dcelery.celery import mq1,mq2,mq3,mq4
mq2.apply_async(priority=5)
mq3.apply_async(priority=9)
mq1.apply_async(priority=6)
mq2.apply_async(priority=5)
mq1.apply_async(priority=6)
mq3.apply_async(priority=9)
mq1.apply_async(priority=6)
mq2.apply_async(priority=5)
mq3.apply_async(priority=9)