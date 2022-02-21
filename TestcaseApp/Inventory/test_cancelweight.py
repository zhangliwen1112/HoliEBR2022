# -*- coding: utf-8 -*- 
# @Time : 2021/2/1 16:22 
# @Author : 张丽雯 
# @File : test_cancelweight.py 
# @中文描述 :  取消称量--取消称量
import pytest
import sys
from src.pageobjectAPP.pageCancelWeight import *
from src.public.common.Close_current_tab import *
from DataApp.CancelWeightData import *

class Test_returned_materials:
    def setup_class(self):
        app_login(username, password)
        login_cancel_weight()


    def teardown_class(self):
        Close_current_tab()
        app_logout()

    def test_login(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        cancel_weight_execute(label3)
