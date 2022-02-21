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
from src.public.common.Login import *
from src.pageobjectAPP.pageMaterial import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
from src.public.common.Close_current_tab import *


addcodedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
addnamedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
editnamedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
copycodedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))


class Test_Material:
    def setup_class(self):
        login_material()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增物料
    def test_add_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_add(addcodedata, addnamedata, adddescdata)
        time.sleep(2)
        assert new_get_text("//div[@row-index='0']//div[@col-id='code']") == addcodedata
        log.info("新增成功 %s" % addcodedata)

    # 搜索物料
    def test_search_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑物料
    def test_edit_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        material_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 复制物料
    def test_copy_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_copy(copycodedata)
        time.sleep(2)
        assert new_page_source(copycodedata)

    # 验证物料
    def test_verify_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        material_verify()
        search_item('编码', addcodedata)
        time.sleep(2)
        assert new_page_source("已验证")
        search_item("编码", ' ')

    # 取消验证物料
    def test_cancelverify_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        material_cancelverify()
        search_item('编码', addcodedata)
        time.sleep(2)
        assert new_page_source("可编辑")
        search_item("编码", ' ')

    # 失效物料
    def test_noeffect_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        material_noeffect()
        search_item('编码', addcodedata)
        time.sleep(2)
        assert new_page_source("失效的")
        search_item("编码", ' ')

    # 生效物料
    def test_effect_material(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        material_effect()
        search_item('编码', addcodedata)
        time.sleep(2)
        assert new_page_source("可编辑")
        search_item("编码", ' ')




if __name__ == '__main__':
    pytest.main(['-s','test_material.py'])
