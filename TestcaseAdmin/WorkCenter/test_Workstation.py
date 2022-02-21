#coding=utf-8

"""
Created on 2020/9/8
@workstationor: lianxiujuan
@desc: 工作站
"""

import pytest
import sys
from src.pageobjectAdmin.pageworkstation import *
from DataAdmin.WorkstationData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_Workstation:
    def test_workstation(self):
        sleep(3)
        login_workstation()
        sleep(2)

    # 新增工作站
    def test_add_workstation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        workstation_add(addnamedata, addcodedata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 搜索工作站
    def test_search_workstation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑工作站
    def test_edit_workstation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        workstation_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除工作站
    def test_delete_workstation(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        workstation_delete()
        time.sleep(2)
        assert new_page_source(addnamedata) == False