# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 17:55 
# @Author : 张丽雯 
# @File : test_ContainerOvercase.py 
# @中文描述 :  结束容器页面

import sys
import pytest
# from DataApp.Containerover import *
from src.public.Logger import *
from src.pageobjectAPP.pageContainerOver import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_Container_Over:
    def setup_class(self):
        app_login(username, password)
        login_container_over()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 取消结束
    def test_Container_Over_001(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_over_cancel()

    # 打印标签
    @pytest.mark.parametrize('num',['1'])
    def test_Container_Over_002(self, num):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_over_label(num)
        container_over_refresh()

    # 归零
    def test_Container_Over_003(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_over_zero()

    # 删除
    def test_Container_Over_004(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_over_delete()

    # 筛选-结束容器为N
    def test_Container_Over_005(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_option('结束容器','N')
        sleep(1)
        assert (is_text_present('N'),'筛选正确！')

    # 结束容器
    def test_Container_Over_006(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_over()

    # 筛选-清除是否结束的筛选条件
    def test_Container_Over_007(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_option('结束容器','---请选择---')
        sleep(1)