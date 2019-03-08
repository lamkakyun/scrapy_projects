# -*- coding: utf-8 -*-

import sqlite3
import time
import mix_config

class ScrapyIpPipeline(object):

    def __init__(self, sqlite_conn):
        self.name = 'ip_pipeline'
        self.sqlite_conn = sqlite_conn

        self.cursor = self.sqlite_conn.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS ip_pool (
        ip_port    CHAR (20) PRIMARY KEY,
        is_https   INT (1),
        hide_level INT (2),
        fail_num   INT (4)   DEFAULT (0),
        uptime     INT (11) 
        );
        """
        self.cursor.execute(sql)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # sqlite_conn = sqlite3.connect(crawler.settings.get('SQLITE_PATH'))
            sqlite_conn = sqlite3.connect(mix_config.MC_IP_DB)
        )

    def open_spider(self, spider):
        print("%s: %s" % (self.name, 'open spider'))

    def close_spider(self, spider):
        print("%s: %s" % (self.name, 'close spider'))
        self.sqlite_conn.close()

    def process_item(self, item, spider):
        if not item:
            return
        
        ip_port = "%s:%s" % (item['ip'].pop(), item['port'].pop())
        is_https = 1 if item['is_https'].pop().upper() == 'HTTPS' else 0
        hide_level = 2 if item['hide_level'] == '高匿' else 1
        uptime = int(time.time())
        
        self.cursor.execute("SELECT * FROM ip_pool WHERE ip_port=?", (ip_port, ))
        result = self.cursor.fetchone()
        if result:
            print("记录已存在: %s" % ip_port)
        else:
            self.cursor.execute("INSERT INTO ip_pool (ip_port, is_https, hide_level, uptime) VALUES (?, ?, ?, ?)", (ip_port, is_https, hide_level, uptime))
            self.sqlite_conn.commit()
            print("记录已添加 : %s" % ip_port)

        return item
