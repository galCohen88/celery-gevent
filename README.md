# celery-gevent
Fix For ack_late bug

Problem:
When using gevent monkey patch and running celery task, tasks are not re-executed after visibility_timeout is expired


# Start the project
virtualenv celeryge

source celeryge/bin/activate

pip install -e .

docker network create celerygevent

docker-compose up

celery -A src.tasks worker -P gevent --loglevel=DEBUG

celery beat -A src.tasks --loglevel=DEBUG
