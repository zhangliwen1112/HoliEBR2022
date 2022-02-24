#coding=utf-8

"""
Created on 2020/9/8
@mimanageor: lianxiujuan
@desc: MI管理
"""

import pytest
import sys
from src.pageobjectAdmin.pageMImanage import *
from DataAdmin.MIData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_MImanage:
    def setup_class(self):
        sleep(2)
        login_mimanage()


    # 新增MI
    def test_add_mimanage(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        mimanage_add(addcodedata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索MI
    def test_search_mimanage(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("MI编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addcodedata in text
        search_item("MI编码", ' ')
        time.sleep(2)

    # 编辑MI
    def test_edit_mimanage(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        mimanage_edit(editdescdata)
        time.sleep(2)
        assert new_page_source(editdescdata)

    # 删除MI管理
    def test_delete_mimanage(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        mimanage_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False
        new_click(promg)


