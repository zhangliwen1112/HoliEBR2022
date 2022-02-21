#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 危险防范信息
"""


import pytest
import sys
from DataApp.RiskpreventionData import *
from src.pageobjectAPP.pageRiskprevention import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
from src.public.common.Close_current_tab import *



class Test_Riskprevention:
    def setup_class(self):
        login_Riskprevention()

    def teardown_class(self):
        Close_current_tab()

    # 新增危险防范信息
    def test_add_riskprevention(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        riskprevention_add(addcodedata, addcdescdata, addedescdata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索危险防范信息
    def test_search_riskprevention(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑危险防范信息
    def test_edit_riskprevention(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        riskprevention_edit(editcdescdata, editcdescdata)
        time.sleep(2)
        assert new_page_source(editcdescdata)

    # 删除危险防范信息
    def test_effect_riskprevention(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        riskprevention_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False




if __name__ == '__main__':
    pytest.main(['-s','test_riskpreventioncase.py'])
