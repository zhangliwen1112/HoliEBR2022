#coding=utf-8

"""
Created on 2020/9/8
@mimanageor: lianxiujuan
@desc: opc设置
"""

import pytest
import sys
from src.pageobjectAdmin.pageOpcset import *
from DataAdmin.OPCsetData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_Opcset:
    def setup_class(self):
        admin_login(username, password)
        login_opcset()

    def teardown_class(self):
        admin_logout()

    # 新增opc设置
    def test_add_opcset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        opcset_add(addnamedata,addcodedata,addaddressdata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索OPC
    def test_search_opcset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("名称", addnamedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addnamedata in text
        search_item("名称", ' ')
        time.sleep(2)

    # 编辑opc设置
    def test_edit_opcset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        opcset_edit(editaddressdata)
        time.sleep(2)
        assert new_page_source(editaddressdata)

    # 锁定opc设置
    def test_lock_opcset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', addnamedata)
        select_item(addnamedata)
        opcset_lock()
        time.sleep(2)
        assert new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="isLocked"]') == '是'
        search_item("名称", ' ')

    # 解锁opc设置
    def test_unlock_opcset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', addnamedata)
        select_item(addnamedata)
        opcset_unlock()
        time.sleep(2)
        assert new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="isLocked"]') == '否'
        search_item("名称", ' ')

    # 删除opc设置
    def test_delete_opcset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        opcset_delete()
        assert new_page_source(addnamedata)




if __name__ == '__main__':
    pytest.main(['-s', 'test_opcsetcase.py'])

