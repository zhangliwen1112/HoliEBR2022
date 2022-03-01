# -*- coding: utf-8 -*- 
# @Time : 2020/11/18 15:26 
# @Author : 张丽雯 
# @File : test_attributivelistcase.py 
# @中文描述 :  属性列表

import sys
import allure
import pytest
from src.pageobjectAPP.pageAttributivelist import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import search_item

@allure.feature('属性列表功能')
class Test_AttributiveList:
    def setup_class(self):
        sleep(1)
        login_attributive_list()
        sleep(1)

    def teardown_class(self):
        Close_current_tab()

    # 新增属性-状态属性、列表属性、数字属性
    @allure.feature('新增属性功能-状态属性、列表属性、数字属性')
    @pytest.mark.parametrize('attributive_code,attributive_type,attributive_name',attributive_list)
    def test_attributive_list_add_001(self,attributive_code,attributive_type,attributive_name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_attributive_list(attributive_code,attributive_type,attributive_name)
        search_item('编码',attributive_code)
        sleep(2)
        assert is_text_present(attributive_name)
        search_item(' ', attributive_code)

    # 新增属性-状态属性、列表属性、数字属性
    @allure.feature('新增属性功能-文本属性')
    @pytest.mark.parametrize('code,type,name,text',attributive_text)
    def test_attributive_list_add_002(self,code,type,name,text):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_attributive_list(code,type,name,text)
        sleep(1)
        assert is_text_present(name)
    # 筛选
    @allure.feature('筛选属性功能')
    def test_attributive_list_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',attributive_code1)
        sleep(1)
        assert is_text_present(attributive_name1)

    # 编辑
    @allure.feature('编辑属性功能')
    def test_attributive_list_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_attributive_list(edit_name)
        sleep(1)
        assert is_text_present(edit_name)

    # 失效
    @allure.feature('失效属性功能')
    def test_attributive_list_noeffect(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        noeffect_attributive_list()
        sleep(1)
        assert is_text_present("已失效")

    # 生效
    def test_attributive_list_effect(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        effect_attributive_list()
        sleep(1)
        assert is_text_present("已创建")


    # 编辑转换状态信息
    def test_status_rule_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_button()
        edit_rule('生产步骤')
        sleep(1)
        assert is_text_present("生产步骤")
        submit_button()

    # 删除转换状态信息
    def test_status_rule_delete(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_button()
        sleep(1)
        delete_rule()
        sleep(1)
        assert (is_text_present("生产步骤"),'删除失败！')
        submit_button()

    # 编辑状态信息
    def test_status_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_button()
        edit_status('xiugai')
        sleep(1)
        assert is_text_present("xiugai")
        submit_button()

    # 删除状态信息
    def test_status_delete(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_button()
        delete_status('否')
        sleep(1)
        assert is_text_present("xiugai")
        submit_button()

    # 复制
    def test_attributive_list_copy(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        copy_attributive_list(copy_code, copy_name)
        sleep(1)
        search_item('编码',copy_code)
        sleep(1)
        assert is_text_present(copy_name)

