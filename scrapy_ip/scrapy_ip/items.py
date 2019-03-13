# -*- coding: utf-8 -*-

import scrapy

class ScrapyIpItem(scrapy.Item):
    ip         = scrapy.Field()
    port       = scrapy.Field()
    hide_level  = scrapy.Field()
    is_https    = scrapy.Field()
    fail_count = scrapy.Field()
    more       = scrapy.Field()
    uptime     = scrapy.Field()

