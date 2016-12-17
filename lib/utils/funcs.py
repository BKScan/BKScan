#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import random, string
from urlparse import urlsplit

def randip():
    """
    获取随机ipv4的ip
    """
    return str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))

def randStr(choices = "", length = 5):
    """
    生成随机字符串
    """
    if choices == "":
        choices = string.ascii_letters + string.digits
    randomstr = ''.join([random.choice(choices) for n in xrange(length)])
    return randomstr

def getHost(url):
    "获取host参数"
    return urlsplit(url).hostname

def getPath(url):
    "获取path信息"
    return urlsplit(url).path

def getParas(url):
    "获取参数字典"
    query = urlsplit(url).query
    tmp = map(lambda x:x.split("=") , query.split("&"))
    result = {}
    for index in tmp:
        result[index[0]] = index[1]
    return result

if __name__ == "__main__":
    pass
