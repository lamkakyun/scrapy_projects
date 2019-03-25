# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy_splash import SplashRequest

class JdspiderSpider(scrapy.Spider):
    name = 'JDSpider'
    allowed_domains = ['jd.com']

    custom_settings = {
        'ITEM_PIPELINES': {},
        'SPLASH_URL': 'http://127.0.0.1:8050',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        }
    }

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        
        req = [
            # url 一样，只返回一个
            scrapy.Request(url='https://www.jd.com/?a=1', callback=self.parse1),
            # scrapy.Request(url='https://www.jd.com/?a=2', callback=self.parse1),
            SplashRequest(url='https://www.jd.com/?a=3', callback=self.parse2, endpoint='render.html',args=splash_args)
        ]
    
        for r in req:
            yield r

    def parse1(self, response):
        print('parse1')
        _f_path = os.path.expanduser('~/Documents/test.html')
        with open(_f_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

    def parse2(self, response):
        print('parse2')
        _f_path = os.path.expanduser('~/Documents/test2.html')
        with open(_f_path, 'w', encoding='utf-8') as f:
            f.write(response.text)