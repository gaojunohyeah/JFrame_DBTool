#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义数据库表字段对象
# ColumnBean
class ColumnBean(object):
    def __init__(self, name, field, type, length, comment,
                 value, allowNull, unique, iskey, autoinc):
        self.name = name
        self.field = field
        self.type = type
        self.length = length
        self.comment = comment
        self.value = value
        self.allowNull = allowNull
        self.unique = unique
        self.iskey = iskey
        self.autoinc = autoinc
