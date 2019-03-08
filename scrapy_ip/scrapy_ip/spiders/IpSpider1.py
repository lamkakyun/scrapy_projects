# -*- coding: utf-8 -*-
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
# from ..misc import config as conf
from scrapy_ip.items import ScrapyIpItem

class Ipspider1Spider(CrawlSpider):
    name = 'IpSpider1'
    allowed_domains = ['www.xicidaili.com']
    start_urls = [
        'http://www.xicidaili.com/nn', # 高匿名
        # 'https://www.xicidaili.com/nt/', # 普通
    ]

    rules = [
        # Rule(LinkExtractor(allow=('http://www.xicidaili.com/nn/\d+$'), callable='parse')),
        # Rule(LinkExtractor(allow=('http://www.xicidaili.com/nt/\d+$')), callable='parse')
    ]

    def parse_start_url(self, response):
        data = response.xpath('//table[@id="ip_list"]/tr')
        
        for d in data:
            item_loader = ItemLoader(item=ScrapyIpItem(), selector=d)
            item_loader.add_xpath('ip', 'td[2]/text()')
            item_loader.add_xpath('port', 'td[3]/text()')
            item_loader.add_xpath('hide_type', 'td[5]/text()')
            item_loader.add_xpath('is_http', 'td[6]/text()')
            item = item_loader.load_item()

            # print(item)

            yield item
