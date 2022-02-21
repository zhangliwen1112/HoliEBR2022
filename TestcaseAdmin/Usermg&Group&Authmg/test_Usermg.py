#coding=utf-8

"""
Created on 2020/9/8
@userpathor: lianxiujuan
@desc: 用户管理
"""

import pytest
import sys
from src.pageobjectAdmin.pageUsermg import *
from DataAdmin.UsermgData import *
from src.public.common.Select_Item import *
from src.pageobjectAdmin.pageOrganize import *
from src.public.common.Search_Item import *



class Test_Usermg:
    def test_login_usermg(self):
        # login_organize_manage()
        # organize_user_add("lian", "lian", '18688888888', '在职', '女')
        sleep(2)
        login_usermg()
        sleep(2)


    # 新增用户
    def test_add_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        user_add(addnamedata, addemaildata, addrfiddata)
        time.sleep(2)
        assert new_page_source(addnamedata)

    # 搜索用户
    def test_search_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("用户名", addnamedata)
        time.sleep(2)
        text = new_get_text(firstdata_admin)
        time.sleep(2)
        assert addnamedata in text
        search_item("用户名", ' ')
        time.sleep(2)

    # 编辑用户
    def test_edit_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        user_edit(editemaildata)
        time.sleep(2)
        assert new_page_source(editemaildata)

    # 激活用户
    def test_active_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        user_active(newpwdata, comfirmpwdata)
        search_item('用户名', addnamedata)
        time.sleep(2)
        assert new_page_source("激活")
        search_item("用户名", ' ')

    # 锁定用户
    def test_lock_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        user_lock()
        search_item('用户名', addnamedata)
        time.sleep(2)
        assert new_page_source("锁定")
        search_item("用户名", ' ')

    # 解锁用户
    def test_unlock_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        user_unlock()
        search_item('用户名', addnamedata)
        time.sleep(2)
        assert new_page_source("激活")
        search_item("用户名", ' ')

    # 删除用户
    def test_delete_user(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addnamedata)
        user_delete()



