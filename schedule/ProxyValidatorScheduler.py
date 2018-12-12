import threading

from apscheduler.schedulers.background import BackgroundScheduler

from db.Redis import RedisClient
from proxy.ProxyValidator import httpsValidator, httpValidator
import time


class ProxyValidatorScheduler(object):
    def __init__(self):
        self.https_list = list()
        self.http_list =list()
        self.raw_https_db = RedisClient("raw_https_proxy")
        self.raw_http_db = RedisClient("raw_http_proxy")

    def load(self):
        for item in self.raw_https_db.sgetall():
            self.https_list.append(item)
        for item in self.raw_http_db.sgetall():
            self.http_list.append(item)

        # 验证完删除，防止积压
        self.raw_https_db.delete()
        self.raw_http_db.delete()

    def run(self, threads=1):
        thread_list = []
        https_list = self.https_list
        http_list = self.http_list
        for index in range(threads):
            thread_list.append(threading.Thread(target=httpsValidator, args=(https_list,)))
        for index in range(threads):
            thread_list.append(threading.Thread(target=httpValidator, args=(http_list,)))
        for thread in thread_list:
            thread.daemon = True
            thread.start()
        for thread in thread_list:
            thread.join()


p = ProxyValidatorScheduler()


def start():
    global p
    p.load()
    p.run()


def run():
    scheduler = BackgroundScheduler()
    scheduler.add_job(start, "interval", minutes=10, name="validateProxy")
    scheduler.start()

    start()

    while True:
        time.sleep(5)



