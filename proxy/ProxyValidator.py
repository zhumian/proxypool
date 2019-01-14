import logging

import requests

import config
from db.Redis import RedisClient

useful_https_db = RedisClient("useful_https_proxy")
useful_http_db = RedisClient("useful_http_proxy")
requests.packages.urllib3.disable_warnings()


def rawHttpsValidator(proxies):
    target = config.ip("https_url")
    for proxy in proxies:
        proxy = proxy.decode("utf-8")
        if validate(proxy=proxy, type="https", target=target):
            useful_https_db.sadd(proxy)


def rawHttpValidator(proxies):
    target = config.ip("http_url")
    for proxy in proxies:
        proxy = proxy.decode("utf-8")
        if validate(proxy=proxy, type="http", target=target):
            useful_http_db.sadd(proxy)


def usefulHttpsValidator(proxies):
    target = config.ip("https_url")
    for proxy in proxies:
        proxy = proxy.decode("utf-8")
        if not validate(proxy=proxy, type="https", target=target):
            useful_https_db.srem(proxy)


def usefulHttpValidator(proxies):
    target = config.ip("http_url")
    for proxy in proxies:
        proxy = proxy.decode("utf-8")
        if not validate(proxy=proxy, type="http", target=target):
            useful_http_db.srem(proxy)


def validate(proxy, type, target):
    proxies = {
        type: "{type}://{proxy}".format(proxy=proxy, type=type)
    }
    try:
        response = requests.get(target, proxies=proxies, verify=False)
        if response.status_code == 200:
            content = str(response.content, encoding="utf-8")
            if proxy.split(":")[0] == content:
                logging.info("result:{result}  proxy:{proxy}".format(result=content, proxy=proxy.split(":")[0]))
                logging.info("[{type}] [{proxy}] validate pass".format(type=type, proxy=proxy))
                return True
        elif response.status_code == 403:
            logging.info("[{type}] [{proxy}] validate fail : 403 forbidden".format(type=type, proxy=proxy))
            return False
    except Exception as e:
        logging.info("[{type}] [{proxy}] validate fail".format(type=type, proxy=proxy))
        return False
    logging.info("[{type}] [{proxy}] validate fail".format(type=type, proxy=proxy))
    return False









