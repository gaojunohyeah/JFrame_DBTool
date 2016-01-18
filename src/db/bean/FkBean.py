#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义数据库表外键对象
# FkBean
class FkBean(object):
    def __init__(self, name, model, type):
        self.name = name
        self.model = model
        self.type = type
