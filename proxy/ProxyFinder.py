import logging
from util.WebParser import loadTree


class ProxyFinder(object):

    """
    西刺代理
    """
    @staticmethod
    def findproxyone(page=10):
        baseUrl = "http://www.xicidaili.com/nn/{page}"
        for p in range(1, page):
            url = baseUrl.format(page=p)
            tree = loadTree(url)
            proxy_list = tree.xpath('.//table[@id="ip_list"]//tr[position()>1]')
            for proxy in proxy_list:
                try:
                   result = proxy.xpath('./td/text()')
                   ip = result[0]
                   port = result[1]
                   type = result[5]
                   yield "{ip}:{port}".format(ip=ip, port=port), type
                except Exception as e:
                   logging.exception(e)

    '''
    66代理（无法识别）
    '''
    @staticmethod
    def findProxyTwo(area=33, page=1):
        for area_index in range(1, area):
            url = "http://www.66ip.cn/areaindex_{}/{}.html".format(area_index, page)
            tree = loadTree(url)
            print(tree)

    '''
    快代理
    '''
    @staticmethod
    def findproxythree(page=2):
        baseUrl = "https://www.kuaidaili.com/free/inha/{page}/"
        for p in range(1, page):
            url = baseUrl.format(page=p)
            tree = loadTree(url)
            trs = tree.xpath('.//table//tr')
            for tr in trs:
                tds = tr.xpath("//td")
                ip = tds[0].text
                port = tds[1].text
                type = tds[3].text
                yield "{ip}:{port}".format(ip=ip, port=port), type

    '''
    云代理
    '''
    @staticmethod
    def findproxyfour(page=4):
        baseUrlList = [
            "http://www.ip3366.net/free/?stype=1&page={page}",  # 国内高匿
            "http://www.ip3366.net/free/?stype=3&page={page}"   # 国外高匿
        ]
        for baseUrl in baseUrlList:
            for p in range(1, page):
                url = baseUrl.format(page=p)
                tree = loadTree(url)
                trs = tree.xpath("//table/tbody//tr")
                for tr in trs:
                    tds = tr.xpath(".//td")
                    ip = tds[0].text
                    port = tds[1].text
                    type = tds[3].text
                    yield "{ip}:{port}".format(ip=ip, port=port), type

    '''
    免费代理IP库
    '''
    @staticmethod
    def findproxyfive(page=10):
        baseUrl = "http://ip.jiangxianli.com/?page={page}"
        for p in range(1, page):
            url = baseUrl.format(page=p)
            tree = loadTree(url)
            trs = tree.xpath("//table/tbody/tr")
            for tr in trs:
                tds = tr.xpath("td")
                ip = tds[1].text
                port = tds[2].text
                type = tds[4].text
                anonymous = tds[3].text
                if anonymous == "高匿":
                    # print("{ip}:{port}".format(ip=ip, port=port))
                    yield "{ip}:{port}".format(ip=ip, port=port), type


if __name__ == '__main__':
    pass


