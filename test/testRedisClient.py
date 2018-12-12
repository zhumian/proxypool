from db.Redis import RedisClient

useful_https_db = RedisClient("useful_https_proxy")
useful_http_db = RedisClient("useful_http_proxy")
raw_https_db = RedisClient("raw_https_proxy")
raw_http_db = RedisClient("raw_http_proxy")


def useful_https():
    print(useful_https_db.sgetall())


def useful_http():
    print(useful_http_db.sgetall())


def raw_https():
    print(raw_https_db.sgetall())


def raw_http():
    print(raw_http_db.sgetall())


def delete():
    useful_http_db.delete()
    useful_https_db.delete()
    raw_http_db.delete()
    raw_https_db.delete()


def get(type):
    if type:
        if type == "https":
            return useful_https_db.sget()
        elif type == "http":
            return useful_http_db.sget()


if __name__ == '__main__':
    delete()