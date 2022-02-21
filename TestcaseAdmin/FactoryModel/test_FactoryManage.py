# coding=utf-8

"""
Created on 2020/9/8
@author: zhangliwen
@desc:HoliEBR-Admin 工厂模型-厂区管理
"""
import sys
import pytest
from src.pageobjectAdmin.pageFactoryManage import *
from DataAdmin.FactoryManageData import *
from src.public.Logger import Log
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *


class Test_Factory_Manage:
    # 登陆环境,进入工厂模型-厂区管理页面
    def test_factory_login(self):
        login_Factory_Manage()
        sleep(2)


    # 新增厂区
    def test_factory_add(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code01,name01)
        search_item('编码', code01)
        assert is_text_present(name01)

    # 筛选 按编码查询
    def test_factory_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码', code01)
        assert is_text_present(name01)

    # 编辑区域
    def test_factory_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_edit(edit_name,Adr1,Adr2,Adr3,Adr4)
        assert new_page_source(edit_name)


    # 关联位置
    def test_factory_relation(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_relation()


    # 去关联
    def test_factory_remove(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_remove()


    # 删除区域
    def test_factory_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_delete()

    # 清除筛选条件
    def test_section_search_clear(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')
        new_click(Factory_Mode)
