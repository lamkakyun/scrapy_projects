# -*- coding: utf-8 -*-
import configparser

def get_misc_conf():
    file_path = './config.ini'
    conf = configparser.ConfigParser()
    conf.read(file_path)
    return conf