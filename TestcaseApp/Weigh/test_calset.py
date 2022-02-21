# -*- coding: utf-8 -*-
# @Time : 2020/10/14 11:01
# @Author : lianxiujuan
# @File : test_Calset.py
# @中文描述 :  校准设置


import pytest
import sys
from DataApp.CalsetData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageCalset import *


class Test_Cal:
    def setup_class(self):
        app_login(username, password)
        login_cal()

    def teardown_class(self):
        app_logout()

    # 天平校准
    def test_cal_balance(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weigh_cal('天平', balance_valid, balance_wtime, balance_step)
        time.sleep(5)
        delete_cal('天平')

    # 地磅校准
    def test_cal_weighbridge(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weigh_cal('地磅', weighbridge_valid, weighbridge_wtime, weighbridge_step)
        time.sleep(5)
        delete_cal('地磅')



if __name__ == '__main__':
    pytest.main(['-s','test_Calset.py'])
