# -*- coding: utf-8 -*- 
# @Time : 2021/4/25 14:06 
# @Author : 张丽雯 
# @File : test_WorkerCenter_abnormal.py 
# @中文描述 :  工作中心-异常场景用例
import sys
import pytest
from src.pageobjectAdmin.pageWorkerCentre import *
from DataAdmin.WorkerCentreData import *
from src.public.Logger import Log
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *

class Test_WorkerCenter():
    # 登陆环境
    def test_worker_add(self):
        sleep(3)
        login_worker_centre()
        sleep(1)
        worker_center_add(add_code1, add_name1)
        sleep(1)
        worker_center_add(add_code2, add_name2)
        sleep(1)
        search_item('编码',add_code1)


    # 新增工作中心-编码为空
    @pytest.mark.parametrize('code,name',code_abnormal_data1)
    def test_workercenter_add_code_abnormal_001(self,code,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code,name)
        sleep(1)
        assert is_text_present('请输入编码')
        new_click(cancel)

    # 新增工作中心-编码超过最大字符
    @pytest.mark.parametrize('code,name', code_abnormal_data2)
    def test_workercenter_add_code_abnormal_002(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code, name)
        sleep(1)
        assert is_text_present('请输入1到20个字符')
        new_click(cancel)

    # 新增工作中心-编码有特殊字符
    @pytest.mark.parametrize('code,name', code_abnormal_data3)
    def test_workercenter_add_code_abnormal_003(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code, name)
        sleep(1)
        assert is_text_present('编码只支持字母数字')
        new_click(cancel)

    # 新增工作中心-编码已重复
    @pytest.mark.parametrize('code,name', code_abnormal_data4)
    def test_workercenter_add_code_abnormal_004(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code, name)
        sleep(1)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 新增工作中心-名称为空
    @pytest.mark.parametrize('code,name',name_abnormal_data1)
    def test_workercenter_add_name_abnormal_001(self,code,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code,name)
        sleep(1)
        assert is_text_present('请输入名称')
        new_click(cancel)

    # 新增工作中心-名称超过最大值
    @pytest.mark.parametrize('code,name', name_abnormal_data2)
    def test_workercenter_add_name_abnormal_002(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code, name)
        sleep(1)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 新增工作中心-名称有特殊字符
    @pytest.mark.parametrize('code,name', name_abnormal_data3)
    def test_workercenter_name_name_abnormal_003(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code, name)
        sleep(1)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 新增工作中心-名称已重复
    @pytest.mark.parametrize('code,name', name_abnormal_data4)
    def test_workercenter_add_name_abnormal_004(self, code, name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(code, name)
        sleep(2)
        assert is_text_present('不能重复')
        sleep(1)
        new_click(cancel)

    # 编辑工作中心-名称为空
    def test_workercenter_edit_name_abnormal_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_edit(name1,'')
        sleep(1)
        assert is_text_present('请输入名称')
        new_click(cancel)

    # 编辑工作中心-名称超过最大值
    def test_workercenter_edit_name_abnormal_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_edit(name2,'')
        sleep(1)
        assert is_text_present('请输入1到100个字符')
        new_click(cancel)

    # 编辑工作中心-名称有特殊字符
    @pytest.mark.parametrize('name',[(name3),(name4)])
    def test_workercenter_edit_code_abnormal_003(self,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_edit(name,'')
        sleep(1)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancel)

    # 编辑工作中心-名称已重复
    def test_workercenter_edit_name_abnormal_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_edit(add_name2,'')
        sleep(1)
        assert is_text_present('已存在,不能重复')
        new_click(cancel)

    # 退出环境
    def test_delete_worker(self):
        worker_center_delete()
        sleep(1)
        search_item('编码', add_code2)
        sleep(1)
        worker_center_delete()
        sleep(1)
        search_item('编码', ' ')
        sleep(1)
        new_click(Work_Centre)
