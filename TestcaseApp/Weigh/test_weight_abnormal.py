# -*- coding: utf-8 -*- 
# @Time : 2021/3/30 16:13 
# @Author : 张丽雯 
# @File : test_weight_abnormal.py 
# @中文描述 :  砝码配置异常场景用例
import sys
import pytest
from DataApp.WeightData import *
from src.public.Logger import *
from src.pageobjectAPP.pageWeight import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import *


class Test_Weight:
    def setup_class(self):
        app_login(username, password)
        login_weight()
        weight_add(weightname1, add_value, add_unit)

    #
    def teardown_class(self):
        weight_delete()
        Close_current_tab()
        app_logout()

    # 新增砝码配置-异常场景-砝码名称异常
    @pytest.mark.parametrize('weightname,add_value,add_unit',name_abnormal_list)
    def test_add_name_abnormal(self,weightname,add_value,add_unit):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_add(weightname,add_value,add_unit)
        assert new_page_source('请按照格式要求填写数据')

    # 新增砝码配置-异常场景-砝码名称异常
    @pytest.mark.parametrize('weightname,add_value,add_unit', add_value_abnormal_list)
    def test_add_value_abnormal(self, weightname, add_value, add_unit):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_add(weightname, add_value, add_unit)
        assert new_page_source('请按照格式要求填写数据')

  # 编辑砝码配置-异常场景-砝码名称异常
    @pytest.mark.parametrize('edit_value,edit_unit', edit_value_abnormal_list)
    def test_edit_value_abnormal(self, edit_value,edit_unit):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_edit(edit_value, edit_unit)
        assert new_page_source('请按照格式要求填写数据')