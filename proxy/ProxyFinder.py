import logging

import config
from util.WebParser import loadTree


class ProxyFinder(object):

    """
    西刺代理
    """
    @staticmethod
    def findProxyOne():
        url = config.proxy("xici")
        tree = loadTree(url)
        proxy_list = tree.xpath('.//table[@id="ip_list"]//tr[position()>1]')
        for proxy in proxy_list:
            try:
               result = proxy.xpath('./td/text()')
               url = result[0]
               port = result[1]
               type = result[5]
               yield url, port, type
            except Exception as e:
               logging.error(e)

    @staticmethod
    def fidnProxyTwo(area=33, page=1):
        for area_index in range(1, area):
            url = "http://www.66ip.cn/areaindex_{}/{}.html".format(area_index, page)
            tree = loadTree(url)
            print(tree)





if __name__ == '__main__':
    ProxyFinder.fidnProxyTwo()



