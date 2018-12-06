from configparser import ConfigParser
import os

cp = ConfigParser()
path = os.path.dirname(os.path.realpath(__file__))
file = path + os.sep + "Proxy.ini"
cp.read(file)


def proxy(key):
    return cp.get("proxy_url", key)


if __name__ == '__main__':
    pass