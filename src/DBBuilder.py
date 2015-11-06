#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import sys

sys.path.append("..")

from src.db.handle import *

# 消息路径
dbPath = "../config"
# 模板路径
templatePath = "../template"

# 获取传入的参数
if (len(sys.argv) == 2):
    dbPath = str(sys.argv[1])

# 修改默认编码格式
reload(sys)
sys.setdefaultencoding('utf8')

print "-------------database build start-------------"
# 读取数据库配置表
tableBeans = DBXmlRead.loadDBXML(dbPath)
# print tableBeans

# 加载模板文件
DBTemRead.DBFileBuild(templatePath, tableBeans)

print "--------------database build end--------------"
