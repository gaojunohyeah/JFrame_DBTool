#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义数据库属性对象
# ColumnBean
class ColumnBean(object):
    def __init__(self, type, name, comment, fields, value, length):
        self.type = type
        self.name = name
        self.comment = comment
        self.fields = fields
        self.value = value
        self.length = length

    def setCanNull(self, notNull):
        if "true" == notNull:
            self.canNull = "false"
        else:
            self.canNull = "true"

    def setIsUnique(self, unique):
        if "true" == unique:
            self.isUnique = "true"
        else:
            self.isUnique = "false"
