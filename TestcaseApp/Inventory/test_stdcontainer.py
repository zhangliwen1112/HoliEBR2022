# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 15:13 
# @Author : 张丽雯 
# @File : test_standardcontainercase.py 
# @中文描述 :  标准容器
import sys
import pytest
from DataApp.stdcontainerData import *
from src.pageobjectAPP.pageStdcontainer import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.public.common.Search_Item import search_item


class Test_StandardContainer:
    def setup_class(self):
        app_login(username, password)
        login_standard_container()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增标准容器
    def test_standardcontainer_add(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name,add_tare)
        sleep(1)
        assert is_text_present(add_name)

    # 筛选容器
    def test_standarcontainer_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', add_name)
        sleep(1)
        assert is_text_present(add_name)

    # 编辑容器
    def test_standardcontainer_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_qty, edit_h, edit_l, edit_w, edit_r, edit_tare, edit_unit)
        sleep(1)
        search_item('名称', edit_name)
        sleep(1)
        assert is_text_present(edit_name)

    # 删除容器
    def test_standardcontainer_delete(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        delete_standard_container()
        sleep(1)
        assert (is_text_present(edit_name), '删除成功！')

    # 清除筛选结果
    def test_standarcontainer_search_clear(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', ' ')
        sleep(1)
        assert new_page_source('C1')
