#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import json

class BKOrderedDict(OrderedDict):
    def __init__(self,items):
        super(BKOrderedDict, self).__init__()
        self.odict = OrderedDict(items)

    def upsert(self, items):
        for k,v in items.items():
            if k not in self.odict.keys():
                self.odict[k]={}
            if isinstance(v, dict): # two level upsert
                for k2,v2 in v.items():
                    self.odict[k][k2] = v2
            else:
                self.odict[k] = v

    def get(self, key):
        if key in self.odict.keys():
            return self.odict[key]
        else:
            return None
    def __getitem__(self, key):
        if key in self.odict.keys():
            return self.odict[key]
        else:
            return None

    def __setitem__(self, key, value):
        self.odict[key] = value

    def items(self):
        return self.odict.items()

    def toJson(self):
        return json.dumps(self.odict)

    # def upsertdefault(self, items):
    #     for k,v in items.items():
    #         if k not in self.odict.keys():
    #             self.odict[k] = {}
    #         self.odict[k]["default"] = v



if __name__ == "__main__":
    bkod = BKOrderedDict({"a":1})
    bkod.upsert({"b":900,"d":10})
    for k,v in bkod.items():
        print k,v
    bkod.upsert({"a":800,"d":123})
    for k,v in bkod.items():
        print k,v
    print bkod.get("z")
