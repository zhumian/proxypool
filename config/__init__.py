from configparser import ConfigParser
import os

cp = ConfigParser()
path = os.path.dirname(os.path.realpath(__file__))
file = path + os.sep + "Proxy.ini"
cp.read(file)


def proxy(key):
    return cp.get("proxy_url", key)


def proxy_methods():
    return cp.options("methods")


def RedisConfig(key):
    return cp.get("redis", key)


def FlaskConfig(key):
    return cp.get("flask", key)



if __name__ == '__main__':
    pass