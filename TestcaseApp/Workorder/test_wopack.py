# -*- coding: utf-8 -*- 
# @Time : 2021/1/6 15:09 
# @Author : 张丽雯 
# @File : test_workpackingcase.py
# @中文描述 :  工单包装
import sys

import pytest

from src.pageobjectAPP.pageWorkorder import *
from src.public.Logger import *
from src.pageobjectAPP.pageWopack import *
from DataApp.WopackData import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_Workpacking:
    def setup_class(self):
        app_login(username, password)

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增包装工单、发布
    def test_workpacking_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_wo()
        sleep(2)
        wo_add('包装工单')
        sleep(3)
        wo_release('包装工单')
        sleep(2)
        Close_current_tab()

    # 进入包装工单页面
    def test_workpacking_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_wopack()
        sleep(2)

    # 耗用
    @pytest.mark.parametrize('num', ['5', '12', '2.215'])
    def test_workpacking_003(self, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wopack_consumed(num, isFinishedContainer)

    # 退回
    @pytest.mark.parametrize('num', ['1', '0.111'])
    @pytest.mark.tuihui
    def test_workpacking_004(self, num):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wopack_returned(num)

    # 调整(前提条件-工单状态为生产终止)
    @pytest.mark.skip
    @pytest.mark.parametrize('num', ['1', '0.111'])
    def test_workpacking_005(self, num):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wopack_changed(num, isFinishedContainer)

    # 按工单编码筛选
    def test_workpacking_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wocode = new_get_text("//div[@role='row' and @row-index='0']//div[@col-id='workOrder']")
        print(wocode)
        search_item('编码',wocode)
        sleep(2)

    # 转移（前提条件：存在生产终止，有退回的的工单）
    @pytest.mark.skip
    def test_worpacking_007(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        woparking_transfer()

    # 清除过滤条件
    def test_worpacking_008(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码', ' ')
