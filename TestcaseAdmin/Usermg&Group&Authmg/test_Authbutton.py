#coding=utf-8

"""
Created on 2020/9/8
@author: lianxiujuan
@desc: 权限按钮
"""

import pytest
import sys
from src.pageobjectAdmin.pageAuthbutton import *
from DataAdmin.AuthbuttonData import *
from src.public.common.Select_Item import *


class Test_Authbutton:
    def test_login_authbutton(self):
        sleep(2)
        login_authbutton()


    # 新增权限按钮
    def test_add_auth(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        auth_add(addcodedata, addnamedata, addintedata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索权限按钮
    def test_search_auth(self):
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑权限按钮
    def test_edit_auth(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        auth_edit(editnamedata, editintedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除权限按钮
    def test_delete_auth(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        auth_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False
        new_click(authmg)

