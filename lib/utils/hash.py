#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
常用hash函数封装
"""
import hashlib


def md5(strPara):
    """
    获取输入字符串strPara的16进制md5值
    """
    m = hashlib.md5()
    m.update(strPara)
    hexHash = m.hexdigest()
    return hexHash
