#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 衡器校准
"""

import pytest
import sys
from src.pageobjectAPP.pageWeighcal import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
from src.public.common.Close_current_tab import *

weighcode = 'cl'

class Test_weighcal:
    def setup_class(self):
        app_login(username, password)
        login_weighcal()

    # def teardown_class(self):
    #     Close_current_tab()
    #     app_logout()

    # # 衡器-校准
    # def test_cal_weighcal(self):
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     weighcal_cal()
    #     time.sleep(2)
    #     # assert new_page_source(weighcode)

    # 衡器-证书
    def test_cert_weighcal(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighcal_cert()
        time.sleep(2)
        # assert new_page_source(editmaxvaluedata)




if __name__ == '__main__':
    pytest.main(['-s','test_weighcal.py'])
