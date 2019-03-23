# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.abspath('../misc'))
import db_helper


def test_get_ip_proxy():
    data = db_helper.get_ip_proxy_list(20)
    for d in data:
        print(d.ip_port)
