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

    def setIndexs(self, indexs):
        self.indexs = indexs
