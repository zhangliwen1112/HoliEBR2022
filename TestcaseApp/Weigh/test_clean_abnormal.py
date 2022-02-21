# -*- coding: utf-8 -*- 
# @Time : 2021/3/30 10:58 
# @Author : 张丽雯 
# @File : test_clean_abnormal.py 
# @中文描述 :  清洁配置异常场景用例
import sys
import pytest
from DataApp.CleanData import *
from src.pageobjectAPP.pageClean import *
from src.public.common.Close_current_tab import Close_current_tab


class Test_Clean:
    def setup_class(self):
        app_login(username, password)
        login_clean()
        clean_add(add_code1, name, ruletype)


    def teardown_class(self):
        clean_delete()
        Close_current_tab()
        app_logout()

    # 新增清洁配置- 规则编码异常场景
    @pytest.mark.parametrize('code,name',code_abnormal_data)
    def test_add_code_abnormal(self,code,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        clean_add(code,name)
        assert new_page_source('请按照格式要求填写数据')

    # 新增清洁配置- 规则名称异常场景
    @pytest.mark.parametrize('code,name',name_abnormal_data)
    def test_add_name_abnormal(self,code,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        clean_add(code,name)
        assert new_page_source('请按照格式要求填写数据')

  # 编辑清洁配置- 规则名称异常场景
    @pytest.mark.parametrize('name',edit_name_abnormal_list)
    def test_edit_name_abnormal(self,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        clean_edit(name)
        assert new_page_source('请按照格式要求填写数据')