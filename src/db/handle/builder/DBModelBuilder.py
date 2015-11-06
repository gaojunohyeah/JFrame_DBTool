#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import BaseBuilder


class DBModelBuilder(BaseBuilder.BaseBuilder):
    def __init__(self, tableBean, env):
        self.templateFile = "db_model.template"
        self.genPath = "../out/app/model/"
        fileName = tableBean.name + ".js"
        BaseBuilder.BaseBuilder.__init__(self, tableBean, self.templateFile, self.genPath, fileName, env)

    def buildDBFile(self):
        try:
            # 渲染模板
            stream = self.template.render(tableBean=self.tableBean)
            # print stream

            # 生成文件
            self.genDBFile(stream)

            return True
        except Exception, e:
            print e
            return False
