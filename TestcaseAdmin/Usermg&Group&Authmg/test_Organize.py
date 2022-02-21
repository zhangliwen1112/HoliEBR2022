# coding=utf-8
"""
Created on 2020/9/3
@author: zhangliwen
@desc:HoliEBR-Admin 组织机构
"""
import sys
from src.pageobjectAdmin.pageOrganize import *
from DataAdmin.OrganizeData import *
from src.public.common.Search_Item import *


class Test_Organize:

    # 进入组织机构页面
    def test_login_organization(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_organize_manage()
        sleep(1)

    # 新增企业
    def test_add_orgcom(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        sleep(1)
        assert new_page_source(add_name)

    # 编辑新增企业
    def test_edit_orgcom(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        new_click(group)
        organize_edit_orgcom(edit_name, edit_type)
        sleep(1)
        assert new_page_source(edit_name)

    # # 新增企业
    # def test_add_orgcom_002(self):
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     organize_add_orgcom(add_name2, code2, add_type2)
    #     sleep(1)
    #     assert new_page_source(add_name2)

    # 刷新左侧组织机构树表结构
    def test_refresh_orgcom(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_refresh_orgcom()

    # 修改用户
    def test_org_user_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sleep(1)
        organize_user_add(users, user_code, tel, status, male)
        sleep(1)
        organize_user_edit(edit_users, edit_tel, edit_status)
        sleep(1)
        assert new_page_source(edit_users)

    # 删除增加的用户
    def test_org_user_delete(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_delete()

    # 刷新列表
    def test_org_refresh(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_refresh()

    # 删除新增企业
    def test_delete_orgcom(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        new_click(group)
        organize_delete_orgcom()
        sleep(1)