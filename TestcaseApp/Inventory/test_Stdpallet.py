#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 标准托盘
"""

import pytest
import sys
from DataApp.StdpalletData import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.pageobjectAPP.pageStdpallet import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *


class Test_stdpallet:
    def setup_class(self):
        app_login(username, password)
        login_stdpallet()

    def teardown_class(self):
        search_item("名称", ' ')
        sleep(1)
        Close_current_tab()
        app_logout()

    # 新增标准托盘
    def test_add_stdpallet(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(addnamedata, addtaredata, addweightdata, addheightdata,
                addlongthdata, addwidthdata, addratiodata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 搜索标准托盘
    def test_search_stdpallet(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("名称", addnamedata)
        time.sleep(2)
        text = new_get_text('//div[@row-index="0"]//div[@aria-colindex="3"]')
        time.sleep(2)
        assert addnamedata in text

    # 编辑标准托盘
    def test_edit_stdpallet(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        stdpallet_edit(editnamedata,edittaredata, editweightdata, editheightdata,
                editlongthdata, editwidthdata, editratiodata)
        time.sleep(1)
        search_item("名称", editnamedata)
        sleep(1)
        assert new_page_source(editnamedata)

    # 删除标准托盘
    def test_delete_stdpallet(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(editnamedata)
        stdpallet_delete()
        time.sleep(2)
        assert new_page_source(editnamedata) == False
