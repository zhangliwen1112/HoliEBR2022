#coding=utf-8

"""
Created on 2021/2/23
@userpathor: lianxiujuan
@desc: 用户管理-异常场景
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
        sleep(2)
        login_organize_manage()
        sleep(2)
        organize_user_add("sss1", "sss1", '18688888888', '在职', '女')
        sleep(2)
        login_usermg()
        sleep(1)


    # 新增用户_用户名 长度超过20、长度小于4、不是以字母开头、含大写字母、含特殊字符
    @pytest.mark.parametrize('usernameerror', [' ', '发电技术开发进度', 'abcdeabcdeabcdeabcde1', 'abc', '!fjldskjf', 'ABC123', 'abc#@urllib3介绍'])
    def test_adduser_usernamerror1(self, usernameerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        user_add(usernameerror, addemaildata, addrfiddata)
        time.sleep(2)
        assert new_page_source('用户名以字母开头，由4-20个小写字母数字组成')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[1])

    # 新增用户_用户名已存在
    def test_adduser_usernamerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        user_add('li01', addemaildata, addrfiddata)
        time.sleep(2)
        assert new_page_source('li01已存在,不能重复')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[1])

    # 新增用户_邮箱格式错误
    @pytest.mark.parametrize('mailerror', [' ', 'abc', 'abc.com', '@a.com', 'jfd@a.'])
    def test_adduser_mailerror(self, mailerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        user_add(addnamedata, mailerror, addrfiddata)
        time.sleep(2)
        assert new_page_source('请输入电子邮箱,例如:name@example.com')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[1])

    # 新增用户_rfid已存在
    def test_adduser_rfiderror(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        user_add(addnamedata, addemaildata, 'c36b6b5b')
        time.sleep(2)
        assert new_page_source('c36b6b5b已存在,不能重复')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[1])

    # 编辑用户_邮箱格式错误
    @pytest.mark.parametrize('mailerror', [' ', 'abc', 'abc.com', '@a.com', 'jfd@a.'])
    def test_edituser_mailerror(self, mailerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        user_edit(mailerror)
        time.sleep(2)
        assert new_page_source('请输入电子邮箱,例如:name@example.com')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[1])

    # 激活用户_密码长度小于6
    def test_activeuser_passwderror1(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item('li01')
        user_active('12', '12')
        time.sleep(2)
        assert new_page_source('至少8位密码')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[2])

    # 激活用户_新旧密码不一致
    def test_activeuser_passwderror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item('li01')
        user_active('222222', '333333')
        time.sleep(2)
        assert new_page_source('两次输入密码不一致')
        time.sleep(1)
        ele = new_find_elements(cancel_button)
        new_click_ele(ele[2])


