# -*- coding: utf-8 -*- 
# @Time : 2021/1/14 10:44 
# @Author : 张丽雯 
# @File : test_MaterialSetcase.py 
# @中文描述 :  物料字段设置用例--异常场景
import sys
import pytest
from DataApp.MaterialSetData import *
from src.pageobjectAPP.pageMaterialSet import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import search_item


class Test_Material_Set:
    def setup_class(self):
        login_Material_Set()
        sleep(1)
        search_item('字段显示名称', '系列')
        sleep(1)

    def teardown_class(self):
        Close_current_tab()

    # 编辑物料字段---修改字段为必填，存在为空的物料数据
    # def test_Material_Set_abnormal(self):
    #     log.info("编辑物料字段%s" % sys._getframe().f_code.co_name)
    #     Material_Set_edit(edit_text1)
    #     assert  new_page_source('该字段存在内容为“空”的物料数据')
    #     sleep(0.5)

    # 设置物料字段默认值--称量间误差异常数值
    @pytest.mark.parametrize('weight_error',weight_error_abnormal_list)
    def test_Material_Set_weight_abnormal(self,weight_error):
        log.info("设置物料字段默认值%s" % sys._getframe().f_code.co_name)
        Material_Set_default(desc_text, material_type, material_unit, material_potency,weight_error)
        sleep(0.5)
        assert is_text_present('请输入整数') or is_text_present('请输入大于-9999，小于9999的整数')
        new_click(no_button)

    # # 设置物料字段默认值--有效期异常数值
    # @pytest.mark.parametrize('desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule',material_validity_abnormal_list)
    # def test_Material_Set_validity_abnormal(self,desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule):
    #     log.info("设置物料字段默认值%s" % sys._getframe().f_code.co_name)
    #     Material_Set_default(desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule)
    #     sleep(0.5)
    #
    #
    # # 设置物料字段默认值--有效期预警异常数值
    # @pytest.mark.parametrize('desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule',alarm_abnormal_list)
    # def test_Material_Set_alarm_abnormal(self,desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule):
    #     log.info("设置物料字段默认值%s" % sys._getframe().f_code.co_name)
    #     Material_Set_default(desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule)
    #     sleep(0.5)
    #
    # # 设置物料字段默认值--取样量异常数据
    # @pytest.mark.parametrize('desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule',qty_abnormal_list)
    # def test_Material_Set_qty_abnormal(self,desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule):
    #     log.info("设置物料字段默认值%s" % sys._getframe().f_code.co_name)
    #     Material_Set_default(desc,type,unit,potency,error,validity,va_unit,alarm,qty,rule)
    #     sleep(0.5)
    #
