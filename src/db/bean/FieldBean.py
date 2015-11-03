#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义table类型column子属性对象
# FieldBean
class FieldBean(object):
    def __init__(self, type, name, comment, value):
        self.type = type
        self.name = name
        self.comment = comment
        self.value = value
