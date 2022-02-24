#coding=utf-8

"""
Created on 2020/9/8
@signruleor: lianxiujuan
@desc: 签名规则
"""

import pytest
import sys

from DataAdmin.SignData import addremarkdata
from src.pageobjectAdmin.pageSign import sign_add, sign_delete
from src.pageobjectAdmin.pageSignrule import *
from DataAdmin.SignruleData import *
from src.public.common.Login import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_Signrule:
    def setup_class(self):
        sleep(2)
        login_signrule()
        sign_add(addnamedata, addremarkdata)

    def teardown_class(self):
        sign_delete()
        sleep(2)


    # 新增签名规则
    def test_add_signrule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        sleep(1)
        signrule_add(addnamedata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 搜索签名规则
    def test_search_signrule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("规则名称", addnamedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addnamedata in text
        search_item("规则名称", ' ')
        time.sleep(2)

    # 编辑签名规则
    def test_edit_signrule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(editruledata)
        select_item(addnamedata)
        signrule_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除签名规则
    def test_delete_signrule(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        # select_item(editruledata)
        select_item(editnamedata)
        signrule_delete()
        time.sleep(2)

