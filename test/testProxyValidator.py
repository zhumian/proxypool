from proxy.ProxyValidator import validate
from util.WebRequest import WebRequest
import logging, json

format = "%(asctime)s - [%(levelname)s] - [%(funcName)s] - %(message)s"
logging.basicConfig(level=logging.INFO, format=format)

wr = WebRequest()

def run():
    proxy = "27.208.24.164:8060"
    type = "http"
    targetUrl = "http://httpbin.org/ip"
    validate(proxy, type, targetUrl)

    proxies = {
        type: "{type}://{url}".format(type=type, url=proxy)
    }
    wr = WebRequest()
    response = wr.get(url=targetUrl, proxies=proxies)
    origin = json.loads(response.content)['origin']
    print(origin)


if __name__ == '__main__':
    run()