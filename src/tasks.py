import time
from src import app
from gevent import monkey
monkey.patch_all()


@app.task(acks_late=True)
def while_true():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print str(count)
