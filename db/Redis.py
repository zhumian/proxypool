import redis
from config import RedisConfig


class RedisClient(object):

    def __init__(self, name):
        self.name = name
        host = RedisConfig("host")
        port = RedisConfig("port")
        self.conn = redis.Redis(host=host, port=port, db=0)

    def hset(self, value):
        self.conn.sadd(self.name, value)

    def hget(self, key):
        return self.conn.hget(self.name, key)

    def hgetall(self):
        return self.conn.hgetall(self.name)

    def hdel(self, key):
        self.conn.hdel(self.name, key)

    def sadd(self, value):
        self.conn.sadd(self.name, value)

    def spop(self, count):
        return self.conn.spop(self.name, count)

    def sget(self, count=None):
        return self.conn.srandmember(self.name, count)

    def sgetall(self):
        return self.conn.smembers(self.name)

    def delete(self):
        return self.conn.delete(self.name)

    def scard(self):
        return self.conn.scard(self.name)


if __name__ == '__main__':
    https_raw_db = RedisClient("https_raw_proxy")
    print(https_raw_db.hgetall())
    print("-----------------------------------")
    http_raw_db = RedisClient("http_raw_proxy")
    list = http_raw_db.hgetall()
    print(http_raw_db.hgetall())





