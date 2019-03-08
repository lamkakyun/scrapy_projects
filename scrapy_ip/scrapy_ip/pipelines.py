# -*- coding: utf-8 -*-

import sqlite3


class ScrapyIpPipeline(object):

    def __init__(self):
        self.name = 'ip_pipeline'

    # @classmethod
    # def from_crawler(cls, crawler):
    #     """ create a pipeline instance"""
    #     # return cls(
    #     #     sqlite_conn = sqlite3.connect(crawler.settings.get('SQLITE_PATH'))
    #     # )
    #     pass

    def open_spider(self, spider):
        print("%s: %s" % (self.name, 'open spider'))

    def close_spider(self, spider):
        print("%s: %s" % (self.name, 'close spider'))

    def process_item(self, item, spider):
        print(item)
        return item
