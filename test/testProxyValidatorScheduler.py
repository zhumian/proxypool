from schedule.ProxyValidatorScheduler import ProxyValidatorScheduler
import logging

logging.basicConfig(level=logging.INFO)


def run():
    p = ProxyValidatorScheduler()
    p.load()
    p.run()


if __name__ == '__main__':
    run()