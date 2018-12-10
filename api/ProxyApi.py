from flask import Flask, request, jsonify
from proxy.ProxyManager import  ProxyManager
from config import FlaskConfig

app = Flask(__name__)
pm = ProxyManager()


@app.route("/<type>/get")
def get(type):
    if type:
        proxy = pm.get(type)
        return proxy.decode("utf-8") if proxy else "no useful proxy"


@app.route("/info")
def info():
    return jsonify(pm.info()
                   )


def run():
    host = FlaskConfig("host")
    port = FlaskConfig("port")
    app.run(host=host, port=port)


if __name__ == '__main__':
    run()


