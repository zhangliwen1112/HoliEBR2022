# -*- coding: utf-8 -*- 
# @Time : 2021/4/25 9:11 
# @Author : 张丽雯 
# @File : test_Device_adnormal.py 
# @中文描述 :  工作中心-外部设备 异常场景用例
import sys
import pytest
from src.pageobjectAdmin.pageDevice import *
from DataAdmin.DeviceData import *
from src.public.common.Search_Item import *


class Test_Device_Manage:
    # 登陆环境
    def test_add_device(self):
        sleep(2)
        login_device_manage()
        sleep(1)
        device_manage_add(device_code01, device_name01, device_type01, device_status01, device_address01)
        device_manage_add(device_code02, device_name02, device_type02, device_status02, device_address02)
        sleep(1)
        search_item('编码', device_code01)


    # 新增设备-编码异常-为空
    @pytest.mark.parametrize(('code, name, type, status, address, des'), code_abnormal_data1)
    def test_device_add_code_abnormal_001(self, code, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(code, name, type, status, address, des)
        assert is_text_present('请输入编码')
        new_click(cancel)

    # 新增设备-编码异常-超过最大字符
    @pytest.mark.parametrize(('code, name, type, status, address, des'), code_abnormal_data2)
    def test_device_add_code_abnormal_002(self, code, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(code, name, type, status, address, des)
        assert is_text_present('请输入1到20个字符')
        new_click(cancel)

    # 新增设备-编码异常-格式不正确
    @pytest.mark.parametrize(('code, name, type, status, address, des'), code_abnormal_data3)
    def test_device_add_code_abnormal_003(self, code, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(code, name, type, status, address, des)
        assert is_text_present('编码只支持字母数字')
        new_click(cancel)

    # 新增设备-编码异常-已重复
    @pytest.mark.parametrize(('code, name, type, status, address, des'), code_abnormal_data4)
    def test_device_add_code_abnormal_004(self, code, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(code, name, type, status, address, des)
        sleep(1)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 新增设备-名称异常-含有特殊字符
    @pytest.mark.parametrize(('code, name, type, status, address, des'), name_abnormal_data1)
    def test_device_add_name_abnormal_001(self, code, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(code, name, type, status, address, des)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 新增设备-名称异常-超过最大值
    @pytest.mark.parametrize(('code, name, type, status, address, des'), name_abnormal_data2)
    def test_device_add_name_abnormal_002(self, code, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_add(code, name, type, status, address, des)
        sleep(1)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 编辑设备-名称异常-含有特殊字符
    @pytest.mark.parametrize(('name,type, status, address, des'), edit_abnormal_data1)
    def test_device_edit_name_abnormal_001(self, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_edit(name, type, status, address, des)
        sleep(1)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 编辑设备-名称异常-超过最大值
    @pytest.mark.parametrize(('name,type, status, address, des'), edit_abnormal_data2)
    def test_device_edit_name_abnormal_002(self, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_edit(name, type, status, address, des)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 编辑设备-名称异常-名称已存在
    @pytest.mark.parametrize(('name,type, status, address, des'), edit_abnormal_data3)
    def test_device_edit_name_abnormal_003(self, name, type, status, address, des):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        device_manage_edit(name, type, status, address, des)
        assert is_text_present('不能重复')
        new_click(cancel)

    def test_delete_device(self):
        device_manage_delete()
        search_item('编码', device_code02)
        sleep(1)
        device_manage_delete()
        search_item('编码', ' ')
        sleep(1)
        new_click(Work_Centre)