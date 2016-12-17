#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BKDataType import BKOrderedDict

class BKScan(object):
    """BKScan Class"""
    # metainfo = BKOrderedDict(dict())
    # options = BKOrderedDict(dict())
    # result = BKOrderedDict(dict())

    def __init__(self):
        self.metainfo = BKOrderedDict({
            "author":"", # 作者信息
            "app":"", # 应用信息
            "version":"", #应用版本信息
            "url":"", #ScanCode对应url信息
            "para":"", #ScanCode对应参数信息
            "type":"", #漏洞类型
            "desc":"", #脚本功能描述
            "scantype":"PAGESCAN", # 扫描选项，PAGESCAN / DIRSCAN
            })
        self.options = BKOrderedDict({
        "url":{
            "required":True,
            "default":"",
            "desc":""
            },
        "schema":{
            "required":False,
            "default":"http",
            "desc":""
            },
        "hostname":{
            "required":False,
            "default":"",
            "desc":""
            },
        "port":{
            "required":False,
            "default":"80",
            "desc":""
            },
        "path":{
            "required":True,
            "default":"",
            "desc":""
            },
        "file":{
            "required":True,
            "default":"",
            "desc":""
            },
        "params":{
            "required":True,
            "default":"",
            "desc":""
            },
        "data":{
            "required":True,
            "default":"",
            "desc":""
            },
        })
        self.result = BKOrderedDict({
        "state": False, # True or False
        "message":"",
        "data":{
            "vuln":{"url":"","para":"","payload":""},
            "db":{"database":"","key":"","value":""},
            "shell":{"path":"","value":""},
            "file":{"name":"","value":""},
            "xss":{"path":"",},
            "etc":{"value":""},
        },
        })

    def pagescan(self):
        pass

    def dirscan(self):
        pass

    def scan(self):
        if self.metainfo["scantype"] == "PAGESCAN":
            self.pagescan()
        else:
            self.dirscan()
