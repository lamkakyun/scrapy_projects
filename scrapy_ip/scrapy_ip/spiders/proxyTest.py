# -*- coding: utf-8 -*-
import scrapy
import mix_config

import os, sys
sys.path.append(os.path.abspath(mix_config.MC_CURRENT_DIR))
import db_helper

# 测试结果确实是成功了
class ProxytestSpider(scrapy.Spider):
    name = 'proxyTest'
    allowed_domains = ['ip.cn']
    test_url = 'https://ip.cn/'

    def start_requests(self):
        print('start_requesting...')

        proxies = db_helper.get_ip_proxy_list(10)
        print(proxies)
        for d in proxies:
            # _ip, _port = d.split(':')
            proxy_url = 'http://%s' % d
            # print(proxy_url)
            yield scrapy.Request(url=self.test_url, callback=self.parse, meta={'proxy': proxy_url})


    def parse(self, response):
        # print(response.body)
        data = response.xpath('//div[@id="result"]//code')
        for d in data:
            print(d.get())
