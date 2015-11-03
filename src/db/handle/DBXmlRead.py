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


# 加载table类型字段的子字段
def loadFieldNode(node):
    type = node.getAttribute('type')
    name = node.getAttribute('name')
    comment = node.getAttribute('comment')

    value = None
    if "table" == type:
        if node.childNodes:
            value = node.childNodes[0].nodeValue.strip()
        else:
            value = {}
    elif "number" == type:
        if node.childNodes:
            value = node.childNodes[0].nodeValue
        else:
            value = 0
    elif "string" == type:
        if node.childNodes:
            value = node.childNodes[0].nodeValue.strip()
        else:
            value = ""

    # 初始化对象
    field = FieldBean.FieldBean(type, name, comment, value)
    return field


# 加载字段
def loadColumnNode(node):
    type = node.getAttribute('type')
    name = node.getAttribute('name')
    comment = node.getAttribute('comment')
    length = node.getAttribute('length')
    notNull = node.getAttribute('notNull')
    unique = node.getAttribute('unique')

    value = None
    fields = []
    if "table" == type:
        if node.childNodes:
            value = node.childNodes[0].nodeValue.strip()
        else:
            value = {}
        # fieldNodes = node.getElementsByTagName("field")
        # for fieldNode in fieldNodes:
        #     # 加载子字段
        #     field = loadFieldNode(fieldNode)
        #     fields.append(field)
    elif "number" == type:
        if node.childNodes:
            value = node.childNodes[0].nodeValue
        else:
            value = 0
    elif "string" == type:
        if node.childNodes:
            value = node.childNodes[0].nodeValue.strip()
        else:
            value = ""

    # 初始化对象
    column = ColumnBean.ColumnBean(type, name, comment, fields, value, length)
    column.setCanNull(notNull)
    column.setIsUnique(unique)
    return column


# 加载数据库文件
def loadDBFile(path):
    dom = minidom.parse(path)

    # 根节点
    root = dom.documentElement

    # 获取表信息
    name = root.getAttribute('name')
    comment = root.getAttribute('comment')
    pk = root.getAttribute('defaultKey')
    isAll = root.getAttribute('isAll')

    tableBean = TableBean.TableBean(name, comment)
    tableBean.setDefaultKey(pk)
    tableBean.setIsallKey(isAll)

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
    # 默认玩家表索引
    if not isAll and not pk:
        indexs.append(["uid"])
    # 手动添加的索引
    childs = root.getElementsByTagName("index")
    for child in childs:
        inames = child.getAttribute('name').split(",")
        indexs.append(inames)
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
