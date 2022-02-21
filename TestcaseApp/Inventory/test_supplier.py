#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 供应商
"""

import pytest
import sys
from DataApp.SupplierData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageSupplier import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_supplier:
    def setup_class(self):
        app_login(username, password)
        login_supplier()

    def teardown_class(self):
        app_logout()

    # 新增供应商
    def test_add_supplier(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        supplier_add(addcodedata, addnamedata, addaddress1data, addaddress2data,
                     addaddress3data, addaddress4data, addleveldata, addemaildata,
                     addphone1data, addphone2data, addfaxdata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索供应商
    def test_search_stdpallet(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑供应商
    def test_edit_supplier(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        supplier_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 删除供应商
    def test_delete_supplier(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        supplier_delete()
        time.sleep(2)
        assert new_page_source(addcodedata) == False




if __name__ == '__main__':
    pytest.main(['-s','test_suppliercase.py'])
