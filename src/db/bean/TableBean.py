#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义数据库对象
# TableBean
class TableBean(object):
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

    def setColumns(self, columns):
        self.columns = columns

    def setIsallKey(self, isAll):
        if "true" == isAll:
            self.isAll = True
        else:
            self.isAll = False

    def setDefaultKey(self, defauleKey):
        if "false" == defauleKey:
            self.defaultKey = False
        else:
            self.defaultKey = True

    def setIndexs(self, indexs):
        self.indexs = indexs
