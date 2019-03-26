# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
import mix_config


class ShanbaySpider(CrawlSpider):
    name = 'shanbay'
    allowed_domains = ['shanbay.com']
    start_urls = ['https://www.shanbay.com/wordbook/category/10/']

    custom_settings = {
        'words.pipelines.WordsPipeline': 300,
    }

    rules = [
        Rule(LinkExtractor(allow=('www.shanbay.com/wordbook/category/\d+')), callback='parse_start_url', follow=True),
    ]

    def parse_start_url(self, response):
        print(response.text)
