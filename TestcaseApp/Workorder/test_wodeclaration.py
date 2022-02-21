# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 13:52 
# @Author : 张丽雯 
# @File : test_Declarationcase.py 
# @中文描述 :  生产声明

import sys
import pytest
from DataApp.WodeclarationData import *
from src.public.Logger import *
from src.pageobjectAPP.pageWodeclaration import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_Declarat:
    def setup_class(self):
        app_login(username, password)
        login_Declaration()

    #
    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 选择要声明的工单
    def test_wo_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码','WO00000065')
    # 生产声明
    def test_Declaration(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        declaration(num, Cnumber)
