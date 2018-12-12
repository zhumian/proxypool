from apscheduler.schedulers.background import BackgroundScheduler
from proxy.ProxyManager import ProxyManager
import time

pm = ProxyManager()


def findProxy():
    pm.load()


def run():
    scheduler = BackgroundScheduler()
    scheduler.add_job(findProxy, "interval", minutes=10, name='findProxy')
    scheduler.start()

    findProxy()

    while True:
        time.sleep(5)
