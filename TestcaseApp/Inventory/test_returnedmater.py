# -*- coding: utf-8 -*- 
# @Time : 2021/2/1 11:27 
# @Author : 张丽雯 
# @File : test_returnedmater.py
# @中文描述 :  取消称量--退料

import pytest
import sys
from src.pageobjectAPP.pageCancelWeight import *
from src.public.common.Close_current_tab import *
from DataApp.CancelWeightData import *

class Test_returned_materials:
    def setup_class(self):
        app_login(username, password)
        login_returned_materials()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 退料
    @pytest.mark.parametrize(('isdeletewo','label','isstore'),returned_data)
    def test_stolocation_move(self,isdeletewo,label,isstore):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        returned_materials_execute(isdeletewo,label,isstore)
