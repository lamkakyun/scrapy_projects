# -*- coding: utf-8 -*-
import os
import telnetlib
import configparser
import threading
import socket
import mix_config

def check_ip_proxy_with_telnet(ip, port, timeout = 5):
    """telnet 太慢了"""
    config = get_config()
    try:
        telnetlib.Telnet(ip, port=int(port), timeout=timeout)
    except Exception as e:
        print('exception:', e)
        return False
    else:
        return True
    
def check_ip_proxy_with_sock(ip, port, timeout = 5):
    """using mutliprocess to check"""
    is_ok = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    p = (ip, port)
    try:
        s.connect(p)
        is_ok = True
    except Exception as e:
        print('exception:', e)
        is_ok = False
    else:
        s.close()
    return is_ok

def get_config():
    conf_path = mix_config.MC_CONF_PATH
    config = configparser.ConfigParser()
    config.read(conf_path)

    conf_dict = config._sections

    return conf_dict