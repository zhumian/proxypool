from proxy.ProxyValidator import validate
from util.WebRequest import WebRequest
import logging

format = "%(asctime)s - [%(levelname)s] - [%(funcName)s] - %(message)s"
logging.basicConfig(level=logging.INFO, format=format)

wr = WebRequest()

def run():
    proxy = "27.208.24.164:8060"
    type = "http"
    targetUrl = "http://httpbin.org/ip"
    validate(proxy, type, targetUrl)


if __name__ == '__main__':
    run()