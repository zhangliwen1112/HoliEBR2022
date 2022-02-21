# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 17:22 
# @Author : 张丽雯 
# @File : test_devicemanagecase.py 
# @中文描述 :  设备管理页面

import sys
import pytest
from DataApp.DeviceManageData import *
from src.public.Logger import *
from src.pageobjectAPP.pageDeviceManage import *


class Test_Device_Manage:
    def setup_class(self):
        app_login(username, password)
        login_device_manage()

    # def teardown_class(self):
    #     app_logout()

    # # 设备不可指派
    # def test_device_manage_unavailable(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_unavailable(unavailable_comments)
    #     sleep(2)
    #     assert "UNAVAILABLE" in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="assignStatus.statusValueName"]')
    #
    # # 设备不可指派
    # def test_device_manage_available(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_available(unavailable_comments)
    #     sleep(2)
    #     assert "AVAILABLE" in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="assignStatus.statusValueName"]')
    #
    # # 设备更新状态为 手动模式
    # def test_device_manage_manual(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_manual()
    #     sleep(2)
    #     assert '手动' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="isAutoUpdate"]')
    #
    # # 设备更新状态为 自动模式
    # def test_device_manage_automatic(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_automatic()
    #     sleep(2)
    #     assert '自动' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="isAutoUpdate"]')
    #
    # # 设备状态为 离线
    # def test_device_manage_offline(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_offline()
    #     sleep(2)
    #     assert '离线' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')
    #
    # # 设备状态为 在线
    # def test_device_manage_online(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_online()
    #     sleep(2)
    #     assert '在线' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')
    #
    # # 打印设备标签
    # def test_device_manage_label(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_label(label_comments)

    # 打印设备标签
    # def test_device_manage_label(self):
    #     log = Log()
    #     log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
    #     device_manage_label(label_comments)

    # 设备编辑
    def test_device_manage_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_edit(label_comments)

