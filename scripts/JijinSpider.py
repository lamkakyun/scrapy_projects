# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class JijinSpider(scrapy.Spider):
    name="jijin"
    allowed_domains = ['danjuanapp.com']
    start_urls = ['https://danjuanapp.com/']

    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

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
            'wait': 0.5
        }
        yield SplashRequest(url='https://danjuanapp.com/', callback=self.parse, endpoint='render.html',args=splash_args)


    def parse(self, response):
        print(response.text)