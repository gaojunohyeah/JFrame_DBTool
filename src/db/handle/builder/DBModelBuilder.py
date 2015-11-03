#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import BaseBuilder


class DBModelBuilder(BaseBuilder.BaseBuilder):
    def __init__(self, tableBean, env):
        self.templateFile = "db_model.template"
        self.genPath = "../out/game/model/"
        fileName = tableBean.name + ".lua"
        BaseBuilder.BaseBuilder.__init__(self, tableBean, self.templateFile, self.genPath, fileName, env)

    # 计算所有类型为table的字段
    def calTableColumns(self, columns):
        tableColumns = []
        for column in columns:
            # 如果是table类型，则添加
            if "table" == column.type:
                tableColumns.append(column)

        return tableColumns

    def buildDBFile(self):
        try:
            # 计算需要列表读取的子属性
            tableColumns = self.calTableColumns(self.tableBean.columns)

            extName = self.tableBean.name.capitalize()
            # 渲染模板
            stream = self.template.render(defaultPK=self.tableBean.defaultKey, tableBean=self.tableBean, extName=extName, tableColumns=tableColumns)
            # print stream

            # 生成文件
            self.genDBFile(stream)

            return True
        except Exception, e:
            print e
            return False
