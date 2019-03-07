# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class Ipspider1Spider(scrapy.Spider):
    name = 'IpSpider1'
    allowed_domains = ['www.xicidaili.com']
    start_urls = [
        'http://www.xicidaili.com/nn', # 高匿名
        'https://www.xicidaili.com/nt/', # 普通
        ]

    rules = [
        # Rule(LinkExtractor(allow=('http://www.xicidaili.com/nn/\d+$'), callable='parse')),
        # Rule(LinkExtractor(allow=('http://www.xicidaili.com/nt/\d+$')), callable='parse')
    ]

    def parse(self, response):
        pass
