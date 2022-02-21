# coding=utf-8

"""
Created on 2020/9/14
@author: zhangliwen
@desc:HoliEBR-Admin 工作中心-外部设备
"""
import sys
import pytest
from src.pageobjectAdmin.pageDevice import *
from DataAdmin.DeviceData import *
from src.public.common.Search_Item import *


class Test_Device_Manage:


    # 进入外部设备页面
    def test_login_Device(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sleep(3)
        login_device_manage()
        assert new_page_source('外部设备')


    # 新增设备
    @pytest.mark.parametrize(('device_code', 'device_name', 'device_type', 'device_status', 'device_address', 'device_des'),add_data)
    def test_device_add(self,device_code, device_name, device_type, device_status, device_address, device_des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(device_code, device_name, device_type, device_status, device_address, device_des)
        assert new_page_source(device_name01)

    # 筛选
    def test_device_search(self):
        log .info('开始执行用例%s' % sys._getframe().f_code.co_name)
        search_item('编码',device_code01)
        assert new_page_source(device_name01)


    # 编辑设备
    def test_device_edit(self):
        log.info('开始执行用例%s' % sys._getframe().f_code.co_name)
        device_manage_edit(edit_name01,edit_type01,edit_status01,edit_address01,edit_des01)
        assert new_page_source(edit_name01)


    # 删除新增设备
    @pytest.mark.parametrize('data',delete_data)
    def test_device_delete(self,data):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码', data)
        device_manage_delete()
        sleep(1)
        assert (is_text_present(data),'删除失败！')

    # 清除筛选条件
    def test_device_search_cancel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')
        new_click(Work_Centre)



