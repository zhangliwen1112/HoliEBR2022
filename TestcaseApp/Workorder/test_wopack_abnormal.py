# -*- coding: utf-8 -*- 
# @Time : 2021/3/29 10:33 
# @Author : 张丽雯 
# @File : test_wopack_abnormal.py
# @中文描述 :  工单包装异常场景用例
import sys
import pytest
from src.pageobjectAPP.pageWorkorder import *
from src.pageobjectAPP.pageWopack import *
from DataApp.WopackData import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_Workpacking:
    def setup_class(self):
        app_login(username, password)
        login_wopack()

    def teardown_class(self):
        Close_current_tab()
        app_logout()


    # 耗用-异常场景-耗用数量异常
    @pytest.mark.parametrize('num,isFinished',num_list_abnormal)
    def test_workpacking_abnormal_001(self,num,isFinished):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sleep(1)
        wopack_consumed(num, isFinished)

    # 退回-异常场景-退回数量异常
    @pytest.mark.parametrize('num', reback_num_list_abnormal)
    def test_workpacking_abnormal_002(self, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wopack_returned(num)
