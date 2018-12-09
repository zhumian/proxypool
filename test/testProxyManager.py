from proxy.ProxyManager import ProxyManager
import logging
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    pm = ProxyManager()
    pm.load()