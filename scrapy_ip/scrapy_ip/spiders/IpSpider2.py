# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy_ip.items import ScrapyIpItem
import mix_config

class Ipspider2Spider(CrawlSpider):
    name = 'IpSpider2'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = [
        'https://www.kuaidaili.com/free/inha/1/',
        'https://www.kuaidaili.com/free/intr/1/'
    ]

    rules = [
        Rule(LinkExtractor(allow='/free/inha/\d+'), callback='parse_start_url', follow=True),
        Rule(LinkExtractor(allow='/free/intr/\d+'), callback='parse_start_url', follow=True),
    ]

    # custom_settings = {
    #     'ITEM_PIPELINES': {}
    # }

    def parse_start_url(self, response):
        print(response.url)
        
        data = response.xpath('//div[@id="list"]//tr')
        for d in data:
            item_loader = ItemLoader(item=ScrapyIpItem(),selector=d)
            item_loader.add_xpath('ip', 'td[1]/text()')
            item_loader.add_xpath('port', 'td[2]/text()')
            item_loader.add_xpath('hide_level', 'td[3]/text()')
            item_loader.add_xpath('is_https', 'td[4]/text()')

            item = item_loader.load_item()

            yield item
