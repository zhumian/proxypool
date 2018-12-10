import logging

from config import proxy_methods
from db.Redis import RedisClient
from proxy.ProxyFinder import ProxyFinder


class ProxyManager(object):
    def __init__(self):
        self.raw_https_db = RedisClient("raw_https_proxy")
        self.raw_http_db = RedisClient("raw_http_proxy")
        self.useful_https_db = RedisClient("useful_https_proxy")
        self.useful_http_db = RedisClient("useful_http_proxy")

    def load(self):
        for method in proxy_methods():
            logging.info("[{method}] : start crawl proxy".format(method=method))
            try:
                for proxy in getattr(ProxyFinder, method)():
                    url = proxy[0]
                    type = proxy[1].lower()
                    if url and type:
                        logging.info("find raw proxy [{type}] [{proxy}]".format(type=type, proxy=url))
                        if type == "https":
                            self.raw_https_db.sadd(url)
                        elif type == "http":
                            self.raw_http_db.sadd(url)
            except Exception as e:
                logging.exception(e)
                logging.error("[{method}] : crawl proxy fail".format(method=method))
    
    def get(self, type):
        if type:
            if type == "https":
                return self.useful_https_db.sget()
            elif type == "http":
                return self.useful_http_db.sget()

    def info(self):
        raw_https_proxy = self.raw_https_db.scard()
        raw_http_proxy = self.raw_http_db.scard()
        useful_https_proxy = self.useful_https_db.scard()
        useful_http_proxy = self.useful_http_db.scard()
        return {
            "raw_https_proxy": raw_https_proxy,
            "raw_http_proxy": raw_http_proxy,
            "useful_https_proxy": useful_https_proxy,
            "useful_http_proxy": useful_http_proxy
        }
                

if __name__ == '__main__':
    pm = ProxyManager()
    pm.load()

