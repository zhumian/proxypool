from lxml import etree
from util.WebRequest import WebRequest
import time, logging


def loadTree(url):
    wr = WebRequest()
    time.sleep(2)
    html = wr.get(url)
    content = html.content
    tree = etree.HTML(content)
    return tree
