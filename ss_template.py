#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.core.BKScan import BKScan
from lib.core.req import post

class ScanCode(BKScan,object):
    """ScanCode Class"""

    def __init__(self):
        super(ScanCode, self).__init__()
        self.metainfo.upsert({})
        self.options.upsert({})
        self.result.upsert({})

    def pagescan(self):
        pass

    def dirscan(self):
        pass


if __name__ == "__main__":
    pass
