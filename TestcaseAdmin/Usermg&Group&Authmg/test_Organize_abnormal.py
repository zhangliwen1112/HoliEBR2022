# -*- coding: utf-8 -*- 
# @Time : 2021/2/23 14:10 
# @Author : 张丽雯 
# @File : test_Organize_abnormal.py 
# @中文描述 :  组织机构异常场景用例
import sys
import pytest
from src.pageobjectAdmin.pageOrganize import *
from DataAdmin.OrganizeData import *
from src.public.common.Search_Item import *


class Test_Organize:
    # 登陆环境
    def test_orgcom_login(self):
        sleep(3)
        login_organize_manage()

    # 新增企业 -- 机构名称异常
    @pytest.mark.parametrize('add_name, code, add_type', add_orgname_abnormal_list)
    def test_add_orgcom_name_abnormal(self, add_name, code, add_type):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        assert new_page_source('组织名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[2])

    # 新增企业 -- 组织编码异常
    @pytest.mark.parametrize('add_name, code, add_type', add_orgcode_abnormal_list)
    def test_add_orgcom_code_abnormal(self, add_name, code, add_type):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        assert new_page_source('组织编码由字母、数字、/_-组成，不能以特殊字符开头')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[2])

    # 新增企业
    def test_add_orgcom(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        sleep(1)
        assert new_page_source(add_name)
        sleep(2)
        new_click(group)

    # 编辑企业 -- 组织名称异常
    @pytest.mark.parametrize('edit_name, edit_type', edit_orgname_abnormal_list)
    def test_edit_orgcom_name_abnormal(self, edit_name, edit_type):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_edit_orgcom(edit_name, edit_type)
        assert new_page_source('组织名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[2])

    # 新增用户--姓名为空
    @pytest.mark.parametrize('users, user_code, tel, status, male', add_user_abnormal_list)
    def test_org_username_add_abnormal(self, users, user_code, tel, status, male):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        assert new_page_source('姓 名由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[4])

    # 新增用户--编码为空
    @pytest.mark.parametrize('users, user_code, tel, status, male', add_code_abnormal_list)
    def test_org_code_add_adnormal(self, users, user_code, tel, status, male):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        assert new_page_source('请输入4-10个英文、数字、下划线、横线')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[4])

    # 新增用户--电话号码为空
    @pytest.mark.parametrize('users, user_code, tel, status, male', add_tel_abnormal_list)
    def test_org_tel_add_abnormal(self, users, user_code, tel, status, male):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        assert new_page_source('请输入正确的11位手机号码')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[4])

    # 新增用户
    def test_add_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        new_click(group)
        sleep(1)
        organize_user_add(users, user_code, tel, status, male)
        sleep(2)
        assert new_page_source(users)

    # 修改用户--姓名为空
    @pytest.mark.parametrize('users, tel, status', edit_user_abnormal_list)
    def test_org_username_edit_abnormal(self, users, tel, status):
        sleep(2)
        organize_user_edit(users, tel, status)
        assert new_page_source('姓 名由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[4])

    # 修改用户--电话号码为空
    @pytest.mark.parametrize('users, tel, status', edit_tel_abnormal_list)
    def test_org_tel_edit_abmormal(self, users, tel, status):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_edit(users, tel, status)
        assert new_page_source('请输入正确的11位手机号码')
        ele = new_find_elements(add_cancel)
        new_click_ele(ele[4])

    def test_orgcom_delete(self):
        organize_user_delete()
        new_click(group)
        organize_delete_orgcom()
