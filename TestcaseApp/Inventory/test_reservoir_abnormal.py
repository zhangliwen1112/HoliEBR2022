# -*- coding: utf-8 -*- 
# @Time : 2021/3/31 14:28 
# @Author : 张丽雯 
# @File : test_reservoir_abnormal.py 
# @中文描述 :  库区管理异常场景测试用例
import sys
import pytest
from DataApp.KuquData import *
from src.pageobjectAPP.pageReservoir import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import search_item


class Test_Reservoir:
    def setup_class(self):
        app_login(username, password)
        login_reservoir()
        kuqu_add(kuqu_code, kuqu_name)
        search_item('编码', kuqu_code)

    #
    def teardown_class(self):
        sleep(0.5)
        kuqu_delete()
        search_item('编码', ' ')
        sleep(0.5)
        Close_current_tab()
        app_logout()

    # 新增库区--编码异常
    @pytest.mark.parametrize('code,name', code_abnormal_list)
    def test_reservoir_code_abnormal(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_add(code, name)

    # 新增库区--名称异常
    @pytest.mark.parametrize('code,name', add_name_abnormal_list)
    def test_reservoir_add_name_abnormal(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_add(code, name)

    # 编辑库区--名称异常
    @pytest.mark.parametrize('name', edit_name_abnormal_list)
    def test_reservoir_edit_name_abnormal(self, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_edit(name)
