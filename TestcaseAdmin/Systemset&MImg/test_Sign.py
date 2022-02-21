#coding=utf-8

"""
Created on 2020/9/8
@signor: lianxiujuan
@desc: 签名设置
"""

import pytest
from src.public.Logger import Log
import sys
from src.pageobjectAdmin.pageSign import *
from DataAdmin.SignData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_Sign:
    def setup_class(self):
        admin_login(username, password)
        login_signset()

    def teardown_class(self):
        admin_logout()

    # 新增签名设置
    def test_add_sign(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sign_add(addnamedata, addremarkdata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 编辑签名设置
    def test_edit_sign(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        sign_edit(editnamedata, editremarkdata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除签名设置
    def test_delete_sign(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(editnamedata)
        sign_delete()
        time.sleep(2)
        assert new_page_source(addnamedata) == False
