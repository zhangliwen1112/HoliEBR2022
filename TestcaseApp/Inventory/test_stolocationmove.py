# -*- coding: utf-8 -*- 
# @Time : 2021/1/29 16:51 
# @Author : 张丽雯 
# @File : test_stolocationmove.py 
# @中文描述 :  库位移动

import pytest
import sys
from src.pageobjectAPP.pageStolocationmove import *
from src.public.common.Close_current_tab import *
from src.public.common.Select_Item import *

class Test_stolocation_move:
    def setup_class(self):
        app_login(username, password)
        login_stolocationmove()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 移动库位
    def test_stolocation_move(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stolocation_move('1234','LOT0000003 0008')
        sleep(2)

    # 查看明细
    def test_stolocation_detail(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stolocation_detail('1234','LOT0000003 0007')
