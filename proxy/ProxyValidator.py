import logging, json

from util.WebRequest import WebRequest
from db.Redis import RedisClient

useful_https_db = RedisClient("useful_https_proxy")
useful_http_db = RedisClient("useful_http_proxy")


def httpsValidator(proxies):
    target = "https://httpbin.org/ip"
    for proxy in proxies:
        proxy = proxy.decode("utf-8")
        if validate(proxy=proxy, type="https", target=target):
            useful_https_db.sadd(proxy)


def httpValidator(proxies):
    target = "http://httpbin.org/ip"
    for proxy in proxies:
        proxy = proxy.decode("utf-8")
        if validate(proxy=proxy, type="http", target=target):
            useful_http_db.sadd(proxy)


def validate(proxy, type, target):
    proxies = {
        type: "{type}://{url}".format(type=type, url=proxy)
    }
    wr = WebRequest()
    try:
        res = wr.get(url=target, proxies=proxies, retry_time=1, timeout=10)
        if res.status_code == 200:
            result_url = json.loads(res.content)['origin']
            if proxy.split(":")[0] == result_url:
                logging.info("url:{url}  proxy:{proxy}".format(url=result_url, proxy=proxy.split(":")[0]))
                logging.info("[{type}] [{proxy}] validate pass".format(type=type, proxy=proxy))
                return True
    except Exception as e:
        logging.info("[{type}] [{proxy}] validate fail".format(type=type, proxy=proxy))
        return False
    logging.info("[{type}] [{proxy}] validate fail".format(type=type, proxy=proxy))
    return False









