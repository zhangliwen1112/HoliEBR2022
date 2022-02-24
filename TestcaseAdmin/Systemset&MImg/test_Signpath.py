#coding=utf-8

"""
Created on 2020/9/8
@signpathpathor: lianxiujuan
@desc: 签名路径
"""

import pytest
import sys
from src.pageobjectAdmin.pageSignpath import *
from DataAdmin.SignpathData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_Signpath:
    def setup_class(self):
        sleep(2)
        login_signpath()


    # 新增签名路径
    def test_add_signpath(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        signpath_add(addcodedata, addnamedata, addleveldata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 搜索签名路径
    def test_search_signpath(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑签名路径
    def test_edit_signpath(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        signpath_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 验证签名路径
    def test_verify_signpath(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        signpath_verify()
        search_item('编码', addnamedata)
        time.sleep(2)
        assert new_page_source("已验证")
        search_item("编码", ' ')

    # 解锁签名路径
    def test_cancelverify_signpath(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        signpath_cancelverify()
        search_item('编码', addnamedata)
        time.sleep(2)
        assert new_page_source("已创建")
        search_item("编码", ' ')

    # 删除签名路径
    def test_delete_signpath(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        signpath_delete()
        time.sleep(2)
        assert new_page_source(addnamedata) == False
        new_click(sysset)




