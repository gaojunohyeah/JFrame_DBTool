#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import os
from xml.dom import minidom
from src.db.bean import *


# 数据库名称字典，用于验证名称的唯一性
TableNameDic = {}


# 获取所有的数据库配置路径
def getXmlFileList(xmlPath):
    # 列出所有文件
    files = os.listdir(xmlPath)
    xmlFiles = []
    # print files
    for file in files:
        truePath = xmlPath + "/" + file
        # 是文件且为xml文件
        if os.path.isfile(truePath) and truePath.endswith(".xml"):
            xmlFiles.append(truePath)

    return xmlFiles

# 加载字段
def loadColumnNode(node):
    name = node.getAttribute('name')
    field = node.getAttribute('field')
    type = node.getAttribute('type')
    length = node.getAttribute('length')
    comment = node.getAttribute('comment')
    value = node.getAttribute('value')
    allowNull = node.getAttribute('allowNull')
    unique = node.getAttribute('unique')
    iskey = node.getAttribute('iskey')
    autoinc = node.getAttribute('autoinc')

    # 初始化对象
    column = ColumnBean.ColumnBean(name, field, type, length, comment,
                                   value, allowNull, unique, iskey, autoinc)
    return column


# 加载数据库文件
def loadDBFile(path):
    dom = minidom.parse(path)

    # 根节点
    root = dom.documentElement

    # 获取表信息
    name = root.getAttribute('name')
    comment = root.getAttribute('comment')

    tableBean = TableBean.TableBean(name, comment)

    # 表名唯一性验证
    if TableNameDic.get(name):
        raise Exception("table name repeat, the table name is", name, " comment is", comment)
    else:
        TableNameDic[name] = name

    # 获取表字段信息
    columnBeans = []

    # 获取表字段节点
    childs = root.getElementsByTagName("column")
    for child in childs:
        # 加载字段
        column = loadColumnNode(child)
        columnBeans.append(column)

    tableBean.setColumns(columnBeans)

    # 获取表索引节点
    indexs = []
    # 手动添加的索引
    childs = root.getElementsByTagName("index")
    for child in childs:
        inames = child.getAttribute('name').split(",")
        iunique = child.getAttribute('unique')

        index = IndexBean.IndexBean(inames, iunique)
        indexs.append(index)
    tableBean.setIndexs(indexs)
    # print indexs

    return tableBean


# 加载所有消息配置
def loadDBXML(dbPath):
    # 获取配置文件
    xmlFiles = getXmlFileList(dbPath)

    TableNameDic = {}

    # 数据库文件加载
    tableBeans = []
    for path in xmlFiles:
        print "load dbconfig file :", path
        tableBeans.append(loadDBFile(path))

    return tableBeans
