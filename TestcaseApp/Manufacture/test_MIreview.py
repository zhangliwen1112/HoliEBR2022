# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 14:21 
# @Author : 张丽雯 
# @File : test_MIreview.py 
# @中文描述 :  批记录复核

import sys
import pytest
from src.pageobjectAPP.pageMIreview import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *
from src.public.common.Sign import *


class Test_MI_review:
    def setup_class(self):
        app_login(username, password)
        login_MI_review()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 筛选
    @pytest.mark.parametrize('lot',['LOT0000060'])
    def test_MI_review_001(self,lot):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('批次号',lot)
        assert new_page_source(lot)

    # 进入批记录复核打开页面
    def test_MI_review_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_review_open()

    # 批准
    def  test_MI_review_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_review_approve()
        sleep(1)
        sign_single('li01','1')
        MI_review_detail('复核说明测试')
        sleep(1)

     # 驳回
    def  test_MI_review_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_review_reject()
        sleep(1)
        sign_single('wang','1')
        MI_review_detail('驳回复核说明测试')
        sleep(1)

    # 重新复核
    def test_MI_review_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_review_re_review()
        MI_review_detail('需重新重新复核备注测试')
        sleep(1)

   # 添加说明
    def test_MI_review_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        MI_review_add_detail()
        MI_review_detail('添加说明测试')
        sleep(1)

    # 关闭工单（全部批准完成后才可关闭工单）
    def test_MI_review_007(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_option('批记录状态','已批准')
        sleep(2)
        search_option('批记录状态', '---请选择---')
        sleep(2)
        MI_review_open()
        MI_review_close_wo()
        sign_double('wang','1','li01','1')
        sleep(1)