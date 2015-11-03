#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import BaseBuilder


class DBManagerBuilder(BaseBuilder.BaseBuilder):
    def __init__(self, tableBean, env):
        self.templateFile = "db_manager.template"
        self.genPath = "../out/game/manager/"
        fileName = tableBean.name.capitalize() + "Manager.lua"
        BaseBuilder.BaseBuilder.__init__(self, tableBean, self.templateFile, self.genPath, fileName, env)

    def buildDBFile(self):
        try:
            extName = self.tableBean.name.capitalize()
            # 渲染模板
            stream = self.template.render(tableBean=self.tableBean, extName=extName)
            # print stream

            # 生成文件
            self.genDBFile(stream)

            return True
        except Exception, e:
            print e
            return False
