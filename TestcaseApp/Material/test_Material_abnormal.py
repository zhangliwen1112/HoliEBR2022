#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 物料管理
"""

import pytest
import sys
import random,string
from DataApp.MaterialData import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.pageobjectAPP.pageMaterial import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
# from src.public.common.Close_current_tab import *


# targetElem = driver.find_element_by_xpath("//*[text()='wl_A2_P_kg_t']")
# targetElem.send_keys(Keys.TAB)

addcodedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))


class Test_Material:
    def setup_class(self):
        login_material()
        sleep(2)

    def teardown_class(self):
        Close_current_tab()

    # 编码异常
    def test_addmaterial_codeerror1(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        codeerror = ['!fjldskjf', 'abc#@urllib3介绍']
        for i in codeerror:
            material_add(i, 'name', 'desc')
            time.sleep(2)
            assert new_page_source('编码由字母、数字、/_-组成，不能以特殊字符开头')
            time.sleep(1)
            new_click(cancel_button)

    # 编码异常
    def test_addmaterial_codeerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_add(' ', 'name', 'desc')
        time.sleep(2)
        assert new_page_source('请输入')
        time.sleep(1)
        new_click(cancel_button)

    # 编码异常
    def test_addmaterial_codeerror3(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_add('1', 'name', 'desc')
        time.sleep(2)
        assert new_page_source('1已存在,不能重复')
        time.sleep(1)
        new_click(cancel_button)

    # 编码异常
    def test_addmaterial_codeerror4(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_add('a'*31, 'name', 'desc')
        time.sleep(2)
        assert new_page_source('输入的字符长度不得超过30')
        time.sleep(1)
        new_click(cancel_button)

    # 名称异常
    def test_addmaterial_nameerror1(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_add(addcodedata, 'a'*101, 'desc')
        time.sleep(2)
        assert new_page_source('输入的字符长度不得超过100')
        time.sleep(1)
        new_click(cancel_button)



