#coding=utf-8

"""
Created on 2020/9/8
@usergpor: lianxiujuan
@desc: 用户组
"""

import pytest
import sys
from src.pageobjectAdmin.pageUsergp import *
from DataAdmin.UsergrpData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *



class Test_Usergp:
    def test_login_usergp(self):
        sleep(2)
        login_usergp()
        sleep(2)

    # 新增用户组
    def test_add_usergp(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        usergp_add(addcodedata, addnamedata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 设置权限
    def test_setauth_usergp(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        usergp_setauth()
        time.sleep(2)
        usergp_setauth()

    # 编辑用户组
    def test_edit_usergp(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        usergp_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除用户组
    def test_delete_usergp(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        usergp_delete()
        time.sleep(2)
        assert new_page_source(addnamedata) == False
        new_click(authmg)
