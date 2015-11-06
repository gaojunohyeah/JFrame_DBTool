#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import BaseBuilder


class DBDaoBuilder(BaseBuilder.BaseBuilder):
    def __init__(self, tableBean, env):
        self.templateFile = "db_dao.template"
        self.genPath = "../out/app/dao/"
        fileName = tableBean.name + "Dao.js"
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
