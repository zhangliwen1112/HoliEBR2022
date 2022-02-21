# -*- coding: utf-8 -*-
# @Time : 2021/4/26 13:53 
# @Author : 张丽雯 
# @File : test_LocationManage_abnormal.py 
# @中文描述 :  工厂模型-位置管理异常场景测试用例
import sys
import pytest
from src.pageobjectAdmin.pageLocationManage import *
from DataAdmin.LocationManageData import *
from src.public.common.Search_Item import *


class Test_Location_Manage:
    # 登陆环境
    def test_location_login(self):
        login_Location_Manage()
        sleep(1)
        Location_Manage_add(code01, name01)
        sleep(1)
        Location_Manage_add(code02, name02)
        sleep(1)
        search_item('编码', code01)



    # 新增位置-编码为空
    @pytest.mark.parametrize(('code', 'name'), code_abnomal_data1)
    def test_location_code_abnormal_001(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('请输入编码')
        new_click(cancel)

    # 新增位置-编码超过最大值
    @pytest.mark.parametrize(('code', 'name'), code_abnomal_data2)
    def test_location_code_abnormal_002(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('请输入1到6个字符')
        new_click(cancel)

    # 新增位置-编码含有特殊字符
    @pytest.mark.parametrize(('code', 'name'), code_abnomal_data3)
    def test_location_code_abnormal_003(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('编码只支持字母数字')
        new_click(cancel)

    # 新增位置-编码已存在
    @pytest.mark.parametrize(('code', 'name'), code_abnomal_data4)
    def test_location_code_abnormal_004(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 新增位置-名称为空
    @pytest.mark.parametrize(('code', 'name'), name_abnomal_data1)
    def test_location_name_abnormal_001(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('请输入名称')
        new_click(cancel)

    # 新增位置-名称超过最大值
    @pytest.mark.parametrize(('code', 'name'), name_abnomal_data2)
    def test_location_name_abnormal_002(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 新增位置-名称含有特殊字符
    @pytest.mark.parametrize(('code', 'name'), name_abnomal_data3)
    def test_location_name_abnormal_003(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 新增位置-名称已存在
    @pytest.mark.parametrize(('code', 'name'), name_abnomal_data4)
    def test_location_name_abnormal_004(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code, name)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 编辑位置-名称为空
    @pytest.mark.parametrize(('name'), edit_name_data1)
    def test_location_edit_name_abnormal_001(self, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_edit(name)
        assert is_text_present('请输入名称')
        new_click(cancel)

    # 编辑位置-名称超过最大值
    @pytest.mark.parametrize(('name'), edit_name_data2)
    def test_location_edit_name_abnormal_002(self, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_edit(name)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 编辑位置-名称有特殊字符
    @pytest.mark.parametrize(('name'), edit_name_data3)
    def test_location_edit_name_abnormal_003(self, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_edit(name)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 编辑位置-名称为空
    @pytest.mark.parametrize(('name'), edit_name_data4)
    def test_location_edit_name_abnormal_004(self, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_edit(name)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    def test_location_delete(self):
        Location_Manage_delete()
        sleep(2)
        search_item('编码', code02)
        sleep(1)
        Location_Manage_delete()
        sleep(1)
        search_item('编码', ' ')
        sleep(2)
        new_click(Factory_Mode)