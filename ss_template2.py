#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.core.BKScan import BKScan
from lib.core.req import post
from lib.utils.hash import md5
from lib.utils.funcs import randStr

class ScanCode(BKScan,object):
    """ScanCode Class"""

    def __init__(self):

        super(ScanCode, self).__init__()

        self.metainfo.upsert({
            "author":"",
            "app":"",
            "version":"",
            "url":"",
            "para":"",
            "type":"",
            "desc":"",
            "scantype":"",
            })

        self.options.upsert({
        "url":{
            "required":True,
            "default":"",
            "desc":""
            },
        })

        self.result.upsert({
        "state": False,
        "message":"",
        "data":{
            "vuln":{"url":"","para":"","payload":""},
            "etc":{"value":""}
        },
        })

    def pagescan(self):
        pass
        
    def dirscan(self):
        pass


if __name__ == "__main__":
    pass
