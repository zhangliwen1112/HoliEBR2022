# -*- coding: utf-8 -*- 
# @Time : 2021/3/23 9:21 
# @Author : 张丽雯 
# @File : test_wocompound_abnormal.py
# @中文描述 :  工单集中、混合异常场景用例
import sys
import pytest
from src.pageobjectAPP.pageWocompound import *
from src.public.common.Close_current_tab import *


class Test_Compound:
    def setup_class(self):
        app_login(username, password)
        login_Compounding()

    #
    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 工单集中-库存ID为空
    @pytest.mark.parametrize('ID', [" "])
    def test_Compound_abnormal_001(self, ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate(ID)
        assert new_page_source('请输入')

   # 工单集中-库存ID不存在
    @pytest.mark.parametrize('ID', ["sss"])
    def test_Compound_abnormal_002(self, ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate(ID)
        assert new_page_source('未查询到此识别号的历史数据')

    # 工单集中-库存ID已集中
    @pytest.mark.parametrize('ID', ["WO0000000500040"])
    def test_Compound_abnormal_003(self, ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate(ID)
        assert new_page_source('此物料已完成集中，该记录不可集中')

    # 工单集中-未有物料可开启时，仍开启集中
    def test_Compound_abnormal_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Concentrate_Open()
        assert new_page_source('开启失败，未有物料可开启集中')

    # 工单混合-输入库存ID为空
    @pytest.mark.parametrize('ID', [" "])
    def test_Compound_abnormal_005(self, ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding(ID)
        assert new_page_source('请输入')

    # 工单混合-输入库存ID不存在
    @pytest.mark.parametrize('ID', ["asd"])
    def test_Compound_abnormal_006(self, ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding(ID)
        assert new_page_source('未查询到此识别号的历史数据')

    # 工单混合-输入库存ID已混合
    @pytest.mark.parametrize('ID', ["WO0000000500001"])
    def test_Compound_abnormal_007(self, ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding(ID)
        assert new_page_source('此物料已完成混合，该记录不可混合')

    # 工单混合-开启混合，未有物料可开启混合
    def test_Compound_abnormal_008(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Compounding_open()
        assert new_page_source('开启失败，未有物料可开启混合')

