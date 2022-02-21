# -*- coding: utf-8 -*- 
# @Time : 2021/7/29
# @Author : lianxiujuan
# @File :
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

    # 移动库位，托盘/容器id异常
    @pytest.mark.parametrize('ciderror',['473824739','FLKDJSFJSKD','*',' '])
    def test_stolocation_move(self,ciderror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stolocation_move_notsubmit('1111',ciderror)
        sleep(2)
        assert new_page_source('不存在该条码的托盘或容器') or new_page_source('请输入托盘/容器 ID')
