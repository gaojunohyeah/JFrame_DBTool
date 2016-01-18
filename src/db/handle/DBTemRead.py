#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import os
import shutil

from jinja2 import *
from src.db.handle.builder import *


# 数据库model文件生成
def DBFileBuild(temPath, tableBeans):
    # 加载模板文件
    env = Environment(loader=FileSystemLoader(temPath))
    # print env.list_templates()

    # 清空并重新生成 数据库生成目录
    outPath = "../out"
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
        os.makedirs(outPath)

    # 循环所有数据库结构
    builder = None
    tableNames = []
    for tableBean in tableBeans:
        tableNames.append(tableBean.name)
        # 数据库结构生成
        builder = DBModelBuilder.DBModelBuilder(tableBean, env)
        if not builder.buildDBFile():
            print "database build error in DBModelBuilder, tableName = " + tableBean.name

        builder = DBDaoBuilder.DBDaoBuilder(tableBean, env)
        if not builder.buildDBFile():
            print "database build error in DBDaoBuilder, tableName = " + tableBean.name

        builder = DBManagerBuilder.DBManagerBuilder(tableBean, env)
        if not builder.buildDBFile():
            print "database build error in DBExtendBuilder, tableName = " + tableBean.name

    builder = DBManagerServicesBuilder.DBManagerServicesBuilder(tableNames, env)
    if not builder.buildDBFile():
        print "database build error in DBManagerServicesBuilder"

    builder = DBDaoServicesBuilder.DBDaoServicesBuilder(tableNames, env)
    if not builder.buildDBFile():
        print "database build error in DBDaoServicesBuilder"

    builder = DBDbsBuilder.DBDbsBuilder(tableBeans, env)
    if not builder.buildDBFile():
        print "database build error in DBDbsBuilder"