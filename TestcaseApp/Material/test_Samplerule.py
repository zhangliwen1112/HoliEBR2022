#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 取样规则
"""

import pytest
import sys
from DataApp.SampleruleData import *
from src.pageobjectAPP.pageSamplerule import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
from src.public.common.Close_current_tab import *



class Test_samplerule:
    def setup_class(self):
        app_login(username, password)
        login_samplerule()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增取样规则
    def test_add_samplerule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        samplerule_add(addcodedata, adddescdata, addenddata, addcontainerdata, addcontainerdata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索取样规则
    def test_search_samplerule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑取样规则
    def test_edit_samplerule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        samplerule_edit(editdescdata)
        time.sleep(2)
        assert new_page_source(editdescdata)

    # 删除取样规则
    def test_delete_samplerule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        samplerule_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False




if __name__ == '__main__':
    pytest.main(['-s','test_samplerulecase.py'])
