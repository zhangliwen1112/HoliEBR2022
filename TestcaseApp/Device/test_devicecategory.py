# -*- coding: utf-8 -*- 
# @Time : 2020/11/19 10:59 
# @Author : 张丽雯 
# @File : test_Eqpcategorycase.py 
# @中文描述 :  接口管理-设备类别接口
import sys

import pytest
from DataApp.EqpcategoryData import *
from src.public.Logger import *
from src.pageobjectAPP.pageEqpcategory import *


class Test_Eqpcategory:
    def setup_class(self):
        app_login(username, password)
        login_Eqp_Category()

    def teardown_class(self):
        app_logout()

    # 新增输出接口
    @pytest.mark.hookwrapper
    def test_add_Eqp_Category(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_Eqp_Category(text)
        edit_Eqp_Category()
        edit_add_Eqp(eqpcode,eqpname)
        change_Eqp_out()
        add_Eqp_out(code, name, type)
        edit_out_Eqp_Category()
        close_Eqp_Category()

    # 编辑输出接口
    def test_edit_Eqp_Category(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_Eqp_Category()
        edit_add_Eqp('1001', "123name")
        change_Eqp_out()
        add_Eqp_out('113', '002name', type)
        edit_Eqp_out('-xiugai','文本')
        edit_out_Eqp_Category()
        close_Eqp_Category()

 # 编辑输出接口
    def test_delete_Eqp_Category(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_Eqp_Category()
        edit_add_Eqp('1002', "1234name")
        change_Eqp_out()
        add_Eqp_out('1123', '003name', type)
        delete_Eqp_out()
        edit_out_Eqp_Category()
        close_Eqp_Category()
