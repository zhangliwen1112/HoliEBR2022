#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 设备类别
"""

import pytest
import sys
from src.public.common.Login import *
from src.pageobjectAPP.pageDeviceclass import *
from src.public.common.Select_Item import *
import random, string
from src.public.common.Search_Item import *


addcodedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
addnamedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
editnamedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
copycodedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))
copynamedata = ''.join(random.sample(string.ascii_letters + string.digits, 4))


class Test_Deviceclass:
    def setup_class(self):
        app_login(username, password)
        login_deviceclass()

    def teardown_class(self):
        app_logout()

    # 新增设备类别
    def test_add_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        deviceclass_add(addcodedata, addnamedata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索设备类别
    def test_search_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑设备类别
    def test_edit_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        deviceclass_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 复制设备类别
    def test_copy_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        deviceclass_copy(copycodedata, copynamedata)
        time.sleep(2)
        assert new_page_source(copycodedata)

    # 失效设备类别
    def test_noeffect_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        select_item(addcodedata)
        deviceclass_noeffect()
        time.sleep(2)
        assert new_page_source("已失效")
        search_item("编码", ' ')
        time.sleep(2)

    # 生效设备类别
    def test_effect_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        select_item(addcodedata)
        deviceclass_effect()
        time.sleep(2)
        assert new_page_source('已创建')




if __name__ == '__main__':
    pytest.main(['-s','test_deviceclass.py'])
