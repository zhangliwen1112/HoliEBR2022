# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 17:36 
# @Author : 张丽雯 
# @File : test_Riskprevention_abnormal.py 
# @中文描述 :  危险防范信息--异常场景
import pytest
import sys
from DataApp.RiskpreventionData import *
from src.pageobjectAPP.pageRiskprevention import *
from src.public.common.Close_current_tab import *
from src.public.common.Select_Item import select_item


class Test_Material_Set:
    def setup_class(self):
        login_Riskprevention()
        riskprevention_add(addcodedata, addcdescdata, addedescdata)

    def teardown_class(self):
        Close_current_tab()

    # 新增危险防范信息--编码异常
    @pytest.mark.parametrize('addcodedata, addcdescdata, addedescdata', code_abnormal_list)
    def test_add_code_abnormal(self, addcodedata, addcdescdata, addedescdata):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        riskprevention_add(addcodedata, addcdescdata, addedescdata)
        assert new_page_source('请按照格式要求填写数据')

    # 新增危险防范信息--中文描述异常
    @pytest.mark.parametrize('addcodedata, addcdescdata, addedescdata', cdesc_add_abnormal_list)
    def test_add_cdesc_abnormal(self, addcodedata, addcdescdata, addedescdata):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        riskprevention_add(addcodedata, addcdescdata, addedescdata)
        assert new_page_source('请按照格式要求填写数据')

    # 新增危险防范信息--英文描述异常
    @pytest.mark.parametrize('addcodedata, addcdescdata, addedescdata', edesc_add_abnormal_list)
    def test_add_edesc_abnormal(self, addcodedata, addcdescdata, addedescdata):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        riskprevention_add(addcodedata, addcdescdata, addedescdata)
        assert new_page_source('请按照格式要求填写数据')

    # 编辑危险防范信息--中文描述异常
    @pytest.mark.parametrize('addcdescdata, addedescdata', cdesc_edit_abnormal_list)
    def test_edit_cdesc_abnormal(self, addcdescdata, addedescdata):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        riskprevention_edit(addcdescdata, addedescdata)
        assert new_page_source('请按照格式要求填写数据')

    # 编辑危险防范信息--英文描述异常
    @pytest.mark.parametrize('addcdescdata, addedescdata', edesc_edit_abnormal_list)
    def test_edit_edesc_abnormal(self, addcdescdata, addedescdata):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        riskprevention_edit(addcdescdata, addedescdata)
        assert new_page_source('请按照格式要求填写数据')

    def test_riskprevention_delete(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(addcodedata)
        riskprevention_delete()
        sleep(1)
