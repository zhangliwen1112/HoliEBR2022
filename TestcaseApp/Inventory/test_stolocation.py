#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 库位
"""

import pytest
import sys
from DataApp.StolocationData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageStolocation import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_stolocation:
    def setup_class(self):
        app_login(username, password)
        login_stolocation()

    # def teardown_class(self):
    #     app_logout()

    # 新增库位
    def test_add_stolocation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stolocation_add1(addcodedata, addnamedata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索库位
    def test_search_stdpallet(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addnamedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addnamedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑库位
    def test_edit_stolocation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        stolocation_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除库位
    def test_delete_stolocation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        stolocation_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False
