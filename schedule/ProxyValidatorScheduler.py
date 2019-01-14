import threading

from apscheduler.schedulers.background import BackgroundScheduler

from db.Redis import RedisClient
from proxy.ProxyValidator import rawHttpsValidator, rawHttpValidator, \
usefulHttpsValidator, usefulHttpValidator
import time


class RawProxyValidatorScheduler(object):
    def __init__(self):
        self.https_list = list()
        self.http_list = list()
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
            thread_list.append(threading.Thread(target=rawHttpsValidator, args=(https_list,)))
        for index in range(threads):
            thread_list.append(threading.Thread(target=rawHttpValidator, args=(http_list,)))
        for thread in thread_list:
            thread.daemon = True
            thread.start()
        for thread in thread_list:
            thread.join()


class UsefulProxyValidatorScheduler(object):
    def __init__(self):
        self.https_list = list()
        self.http_list = list()
        self.useful_https_db = RedisClient("useful_https_proxy")
        self.useful_http_db = RedisClient("useful_http_proxy")

    def load(self):
        for item in self.useful_https_db.sgetall():
            self.https_list.append(item)
        for item in self.useful_http_db.sgetall():
            self.http_list.append(item)

    def run(self, threads=1):
        thread_list = []
        https_list = self.https_list
        http_list = self.http_list
        for index in range(threads):
            thread_list.append(threading.Thread(target=usefulHttpsValidator, args=(https_list,)))
        for index in range(threads):
            thread_list.append(threading.Thread(target=usefulHttpValidator, args=(http_list,)))
        for thread in thread_list:
            thread.daemon = True
            thread.start()
        for thread in thread_list:
            thread.join()


p1 = RawProxyValidatorScheduler()
p2 = UsefulProxyValidatorScheduler()


def raw_start():
    global p1
    p1.load()
    p1.run()


def useful_start():
    global p2
    p2.load()
    p2.run()


def run():
    scheduler = BackgroundScheduler()
    scheduler.add_job(raw_start, "interval", minutes=10, name="validateRawProxy")
    scheduler.add_job(useful_start, "interval", minutes=30, name="validateUsefulProxy")
    scheduler.start()

    raw_start()

    while True:
        time.sleep(5)



