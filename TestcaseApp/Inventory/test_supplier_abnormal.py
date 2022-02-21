# -*- coding: utf-8 -*- 
# @Time : 2021/3/31 9:15 
# @Author : 张丽雯 
# @File : test_supplier_abnormal.py 
# @中文描述 :  供应商信息异常场景用例
import pytest
import sys
from DataApp.SupplierData import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.pageobjectAPP.pageSupplier import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_supplier:
    def setup_class(self):
        app_login(username, password)
        login_supplier()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    @pytest.mark.parametrize('code, name', [(addcodedata, addnamedata), (add_code1, add_name1)])
    def test_add_code(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        supplier_add(code, name)

    # 新增供应商-编码异常
    @pytest.mark.parametrize('code, name',code_abnormal_list)
    def test_add_code_abnormal(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        supplier_add(code, name)
        assert new_page_source('请按照格式要求填写数据')

    # 新增供应商-名称异常
    @pytest.mark.parametrize('code, name', name_abnormal_list)
    def test_add_name_abnormal(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        supplier_add(code, name)
        assert new_page_source('请按照格式要求填写数据')

    # 编辑供应商-名称异常
    @pytest.mark.parametrize('name', edit_name_abnormal)
    def test_edit_name_abnormal(self, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        supplier_edit(name)
        assert new_page_source('请按照格式要求填写数据')

    @pytest.mark.parametrize('code', [addcodedata, add_code1])
    def test_delete_code(self,code):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(code)
        sleep(0.5)
        supplier_delete()
