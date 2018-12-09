from multiprocessing import Process
from schedule.ProxyValidatorScheduler import run as ProxyValidatorScheduler
from schedule.ProxyFindScheduler import run as ProxyFindScheduler
from api.ProxyApi import run as ProxyApi
import logging

logging.basicConfig(level=logging.INFO)


def run():
    process_list = []
    p1 = Process(target=ProxyApi, name='ProxyApi')
    p2 = Process(target=ProxyFindScheduler, name='ProxyFindScheduler')
    p3 = Process(target=ProxyValidatorScheduler, name='ProxyValidatorScheduler')
    process_list.append(p1)
    process_list.append(p2)
    process_list.append(p3)

    for process in process_list:
        process.daemon = True
        process.start()

    for process in process_list:
        process.join()


if __name__ == '__main__':
    run()