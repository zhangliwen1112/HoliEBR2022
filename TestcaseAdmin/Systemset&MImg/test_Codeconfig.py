#coding=utf-8

"""
Created on 2020/9/15
@author: lianxiujuan
@desc: 编码配置
"""

import pytest
import sys
from src.pageobjectAdmin.pageCodeconfig import *
from DataAdmin.CodeconfigData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *


class Test_Codeconfig:
    def setup_class(self):
        admin_login(username, password)
        login_codeconfig()

    # 新增编码配置
    def test_add_codeconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        codeconfig_add(addcodedata, addnamedata, adddescdata, addcirclewaydata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索编码配置
    def test_search_codeconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑编码配置
    def test_edit_codeconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        codeconfig_edit(editnamedata, editdescdata, editcirclewaydata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 重置编码配置
    def test_reset_codeconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        codeconfig_reset()

    # 删除编码配置
    def test_delete_codeconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        codeconfig_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False




if __name__ == '__main__':
    pytest.main(['-s', 'test_Codeconfigcase.py'])