#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 设备配置
"""

import pytest
import sys
from src.public.common.Login import *
from src.pageobjectAPP.pageDeviceconfig import *
from src.public.common.Select_Item import *
import string, random
from src.public.common.Search_Item import *


addcodedata = ''.join(random.sample(string.digits + string.ascii_letters, 4))
addnamedata = ''.join(random.sample(string.digits + string.ascii_letters, 4))
editnamedata = ''.join(random.sample(string.digits + string.ascii_letters, 4))
copycodedata = ''.join(random.sample(string.digits + string.ascii_letters, 4))
copynamedata = ''.join(random.sample(string.digits + string.ascii_letters, 4))


class Test_deviceconfig:
    def setup_class(self):
        app_login(username, password)
        login_deviceconfig()

    def teardown_class(self):
        app_logout()

    # 新增设备配置
    def test_add_deviceconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        deviceconfig_add(addcodedata, addnamedata)
        time.sleep(2)
        assert new_page_source(addcodedata)

    # 搜索设备配置
    def test_search_deviceclass(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert addcodedata in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑设备配置
    def test_edit_deviceconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        deviceconfig_edit(editnamedata)
        time.sleep(2)
        assert new_page_source(editnamedata)

    # 复制设备配置
    def test_copy_deviceconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        deviceconfig_copy(copycodedata, copynamedata)
        time.sleep(2)
        assert new_page_source(copycodedata)

    # 失效设备配置
    def test_noeffect_deviceconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        select_item(addcodedata)
        deviceconfig_noeffect()
        time.sleep(2)
        assert new_page_source("已失效")
        search_item("编码", ' ')
        time.sleep(2)

    # 生效设备配置
    def test_effect_deviceconfig(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", addcodedata)
        time.sleep(2)
        select_item(addcodedata)
        deviceconfig_effect()
        time.sleep(2)
        assert new_page_source('已创建')




if __name__ == '__main__':
    pytest.main(['-s','test_deviceconfigcase.py'])
