# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 14:27 
# @Author : 张丽雯 
# @File : test_ContainerSamplecase.py 
# @中文描述 :  容器取样页面
import sys
import pytest
from DataApp.ContainerSampleData import *
from src.pageobjectAPP.pageContainerSample import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_Container_Sample:
    def setup_class(self):
        app_login(username, password)
        login_container_manage()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 容器取样
    @pytest.mark.parametrize('num',['0.001','0.001'])
    def test_Container_Sample_001(self,num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_sample(num,state)


    # 容器锁定
    def test_Container_Sample_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_lock()
        sleep(1)
        assert new_page_source('锁定')

    # 容器驳回
    def test_Container_Sample_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_reject()
        sleep(1)
        assert new_page_source('驳回')
