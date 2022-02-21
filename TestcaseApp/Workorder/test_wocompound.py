# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 16:09 
# @Author : 张丽雯 
# @File : test_compoundingcase.py 
# @中文描述 :  工单集中、混合
import sys

import pytest
from src.public.Logger import *
from src.pageobjectAPP.pageWocompound import *
from src.public.common.Close_current_tab import *


class Test_Compound:
    def setup_class(self):
        app_login(username, password)
        login_Compounding()

    #
    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 工单集中-通过输入库存ID集中
    @pytest.mark.parametrize('ID', ["WO0000000500002", "WO0000000500019","WO0000000500020"])
    def test_Compound_001(self, ID):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate(ID)

    # 工单集中-开启集中
    def test_Compound_002(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate_Open()

    # 工单集中-强制集中
    def test_Compound_003(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate_Force()

    # 工单混合-通过输入库存ID混合
    @pytest.mark.parametrize('ID', ["WO0000000500020", "WO0000000500021"])
    def test_Compound_004(self, ID):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding(ID)

    # 工单混合-强制混合
    def test_Compound_005(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding_Force()

    # 工单混合-开启混合
    def test_Compound_006(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding_open()
