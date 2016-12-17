#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BKScan入口
"""
import argparse, sys, os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ss", help="scan file")
    args = parser.parse_args(args=sys.argv[1:3])

    if args.ss:
        try:
            sspara = args.ss.replace("&","").replace("|","").replace("..","")
            ssfile = os.path.abspath(args.ss.replace(".py","").replace(".","/")+".py")
            if os.path.exists(ssfile):
                import imp
                tmpsspara = ssfile
                if "/" == ssfile[0]:
                    tmpsspara = ssfile[1:]
                try:
                    ssModule = imp.load_source(tmpsspara.replace(".py","").replace("/","_"),ssfile)
                except ImportError:
                    # import 失败，创建__init__.py
                    initpath =os.path.join(os.path.split(ssfile)[0],"__init__.py")
                    if not os.path.exists(initpath):
                        open(initpath, 'a').close()
                    ssModule = imp.load_source(tmpsspara.replace(".py","").replace("/","_"),ssfile)

                ssInstance = ssModule.ScanCode()
                for option,value in ssInstance.options.items():
                    parser.add_argument("-{}".format(option), default=value["default"], help=value["desc"])

                args_new = parser.parse_args()

                for option, value in ssInstance.options.items():
                    ssInstance.options.upsert({option: {"default":args_new.__dict__[option],}})

                ssInstance.scan()
                sys.stdout.write(ssInstance.result.toJson())

        except Exception as e:
            # print repr(e)
            sys.stderr.write(repr(e))
