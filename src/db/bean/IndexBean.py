#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义数据库表索引对象
# IndexBean
class IndexBean(object):
    def __init__(self, names, unique):
        self.names = names
        self.unique = unique
