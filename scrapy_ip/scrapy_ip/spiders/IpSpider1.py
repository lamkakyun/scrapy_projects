# -*- coding: utf-8 -*-
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy_ip.items import ScrapyIpItem
import mix_config

class Ipspider1Spider(CrawlSpider):
    name = 'IpSpider1'
    allowed_domains = ['www.xicidaili.com']
    start_urls = [
        'http://www.xicidaili.com/nn', # 高匿名
        'https://www.xicidaili.com/nt/', # 普通
    ]

    rules = [
        Rule(LinkExtractor(allow=('www.xicidaili.com/nn/\d+')), callback='parse_start_url', follow=True),
        Rule(LinkExtractor(allow=('www.xicidaili.com/nt/\d+')), callback='parse_start_url', follow=True)
    ]

    def parse_start_url(self, response):

        data = response.xpath('//table[@id="ip_list"]/tr')
        
        print(response.url)
        for d in data:
            item_loader = ItemLoader(item=ScrapyIpItem(), selector=d)
            item_loader.add_xpath('ip', 'td[2]/text()')
            item_loader.add_xpath('port', 'td[3]/text()')
            item_loader.add_xpath('hide_level', 'td[5]/text()')
            item_loader.add_xpath('is_https', 'td[6]/text()')
            item = item_loader.load_item()

            # print(item)

            yield item
