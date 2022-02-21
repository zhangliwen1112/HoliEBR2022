# -*- coding: utf-8 -*-
# @Time : 2021/4/27 16:36 
# @Author : 张丽雯 
# @File : test_FactoryManage_abnormal.py 
# @中文描述 :  工厂模型-厂区管理异常场景测试用例
import sys
import pytest
from src.pageobjectAdmin.pageFactoryManage import *
from DataAdmin.FactoryManageData import *
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *

class Test_Company_Manage_Abnormal:
    # 登陆环境,进入工厂模型-厂区管理页面
    def test_factory_login(self):
        login_Factory_Manage()
        sleep(2)
        Factory_Manage_add(code01, name01)
        sleep(1)
        Factory_Manage_add(code02, name02)
        sleep(1)
        search_item('编码', code01)

    # 新增厂区-编码为空
    @pytest.mark.parametrize(('code', 'name'), add_code_data1)
    def test_factory_code_abnormal_001(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('请输入编码')
        new_click(cancel)

    # 新增厂区-编码不符合长度要求
    @pytest.mark.parametrize(('code', 'name'), add_code_data2)
    def test_factory_code_abnormal_002(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('请输入2个字符')
        new_click(cancel)

    # 新增厂区-编码含有特殊字符
    @pytest.mark.parametrize(('code', 'name'), add_code_data3)
    def test_factory_code_abnormal_003(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('编码只支持字母数字')
        new_click(cancel)

    # 新增厂区-编码重复
    @pytest.mark.parametrize(('code', 'name'), add_code_data4)
    def test_factory_code_abnormal_004(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 新增厂区-编码为空
    @pytest.mark.parametrize(('code', 'name'), add_code_data5)
    def test_factory_code_abnormal_005(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert new_get_text("//div[@class='ivu-form-item-error-tip']")=='请输入'
        new_click(cancel)

    # 新增厂区-名称为空
    @pytest.mark.parametrize(('code', 'name'), add_name_data1)
    def test_factory_name_abnormal_001(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('请输入名称')
        new_click(cancel)

    # 新增厂区-名称超过最大值
    @pytest.mark.parametrize(('code', 'name'), add_name_data2)
    def test_factory_name_abnormal_002(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 新增厂区-名称含有特殊字符
    @pytest.mark.parametrize(('code', 'name'), add_name_data3)
    def test_factory_name_abnormal_003(self,code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 新增厂区-名称已存在
    @pytest.mark.parametrize(('code', 'name'), add_name_data4)
    def test_factory_name_abnormal_004(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_add(code, name)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 编辑厂区-名称为空
    @pytest.mark.parametrize(('name'), edit_name_data1)
    def test_factory_edit_name_abnormal_001(self,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_edit(name)
        assert is_text_present('请输入名称')
        new_click(cancel)

    # 编辑厂区-名称超过最大值
    @pytest.mark.parametrize(('name'), edit_name_data2)
    def test_factory_edit_name_abnormal_002(self,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_edit(name)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 编辑厂区-名称有特殊字符
    @pytest.mark.parametrize(('name'), edit_name_data3)
    def test_factory_edit_name_abnormal_003(self,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_edit(name)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 编辑厂区-名称为空
    @pytest.mark.parametrize(('name'), edit_name_data4)
    def test_factory_edit_name_abnormal_004(self,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Factory_Manage_edit(name)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    def test_factory_delete(self):
        Factory_Manage_delete()
        search_item('编码', code02)
        sleep(1)
        Factory_Manage_delete()
        sleep(1)
        search_item('编码', ' ')
        sleep(2)
        new_click(Factory_Mode)
