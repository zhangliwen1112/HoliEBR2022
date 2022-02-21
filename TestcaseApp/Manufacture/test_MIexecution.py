# -*- coding: utf-8 -*- 
# @Time : 2021/1/12 10:58 
# @Author : 张丽雯 
# @File : test_MIexecutioncase.py 
# @中文描述 :  MI执行-gongxu MI执行

import sys
import pytest

from src.pageobjectAPP.pageWorkorder import *
from src.pageobjectAPP.pageMIexecution import *
from src.public.common.Close_current_tab import *
from src.public.common.Sign import *


class Test_MI_Execution:
    def setup_class(self):
        app_login(username, password)

    def teardown_class(self):
        app_logout()

    # 新增生产工单、发布
    def test_workpacking_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_wo()
        sleep(2)
        wo_add('生产工单')
        sleep(3)
        wo_release('生产工单','import')
        sleep(2)
        Close_current_tab()

    # 选择工单执行MI
    def test_MI_Execution_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_MI_execution()
        sleep(1)
        MI_execution_wo()

    # 开始执行MI
    def test_MI_Execution_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_start()

    # 上传文件
    def test_MI_Execution_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_upfile('培训效果评估表.docx')
        MI_execution_next(0)

    # 工序不可编辑，直接执行下一步
    def test_MI_Execution_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_next(1)

    # text组件，输入内容
    def test_MI_Execution_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_text('text文本测试，最长字段是50字符,text文本测试，最长字段是50字符,text文本测试，最长1')
        MI_execution_next(2)

    # 多行文本组件，输入内容
    def test_MI_Execution_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_multitext('1、满装\n2、防潮\n3、多行文本测试')
        MI_execution_next(3)

    # 卡片next执行
    def test_MI_Execution_007(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_next(4)

    # 数字组件执行
    def test_MI_Execution_008(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_number('10.23')
        MI_execution_next(5)

    # 计算、时间、日期、下拉框组件，直接执行下一步
    def test_MI_Execution_009(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_next(6)
        MI_execution_next(7)
        MI_execution_next(8)
        MI_execution_next(9)
        MI_execution_next(10)

    # 多选框组件执行
    def test_MI_Execution_010(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_multiselect(1)
        MI_execution_multiselect(2)
        MI_execution_next(11)

    # 签名-双签名（管理员+普通用户）
    def test_MI_Execution_011(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_sign_button()
        sign_double('wang', '1', 'li01','1')

    # 强制执行组件执行
    def test_MI_Execution_012(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_force('强制执行组件force')
        MI_execution_next(12)
        sign_double('wang', '1', 'li01','1')

    # 警示组件alert执行
    def test_MI_Execution_013(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_alert('偏差', '微小', '警示组件测试，选择偏差')
        MI_execution_next(13)

    # 快速称量
    def test_MI_Execution_014(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_execution_scale()
        MI_execution_next(14)
        sleep(2)
        # 第二个工序执行
        MI_execution_next(0)
