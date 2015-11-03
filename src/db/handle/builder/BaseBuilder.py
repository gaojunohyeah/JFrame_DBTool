#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import os


# 数据库model生成基类
# tableBean 数据库结构数据对象
# templateFile 数据库模板文件名称
# genPath 数据库类生成路径
# template 模板渲染对象
class BaseBuilder(object):
    def __init__(self, tableBean, temFile, genPath, fileName, env):
        self.tableBean = tableBean
        self.templateFile = temFile
        self.genPath = genPath
        self.fileName = fileName
        self.template = env.get_template(self.templateFile)

    # 生成消息文件基类方法
    def buildDBFile(self):
        return True

    # 写入消息文件
    def genDBFile(self, stream):
        # 路径不存在，则创建对应文件
        if not os.path.exists(self.genPath):
            os.makedirs(self.genPath)

        # 打开文件
        filePath = self.genPath + self.fileName
        print "write database file :", filePath
        file = open(filePath, "w")
        file.write(stream)
        file.close()

        return
