# -*- coding: utf-8 -*-

import scrapy

class ScrapyIpItem(scrapy.Item):
    ip         = scrapy.Field()
    port       = scrapy.Field()
    hide_type  = scrapy.Field()
    is_http    = scrapy.Field()
    fail_count = scrapy.Field()
    more       = scrapy.Field()
    uptime     = scrapy.Field()

