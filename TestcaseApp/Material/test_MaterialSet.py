# -*- coding: utf-8 -*- 
# @Time : 2021/1/14 10:44 
# @Author : 张丽雯 
# @File : test_MaterialSetcase.py 
# @中文描述 :  物料字段设置用例
import sys
import pytest
from DataApp.MaterialSetData import *
from src.public.Logger import *
from src.pageobjectAPP.pageMaterialSet import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import search_item
from src.public.common.elements import alert_txt


class Test_Material_Set:
    def setup_class(self):
        login_Material_Set()

    def teardown_class(self):
        Close_current_tab()


    # 按物料名称筛选
    def test_Material_Set_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('字段显示名称',search_value)
        sleep(2)
        assert new_page_source(search_value)

    # 编辑物料字段
    def test_Material_Set_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Material_Set_edit(edit_text1,edit_text2)
        assert "保存成功" in new_get_text(alert_txt)

    # 取消筛选结果
    def test_Material_Set_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('字段显示名称',' ')
        sleep(1)
        assert new_page_source('系列')

    # 设置物料字段默认值
    def test_Material_Set_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Material_Set_default(desc_text,material_type,material_unit,material_potency,error,material_validity,va_unit,alarm,qty,rule)
        assert "保存成功" in new_get_text(alert_txt)



