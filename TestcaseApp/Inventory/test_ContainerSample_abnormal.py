# -*- coding: utf-8 -*- 
# @Time : 2021/8/4
# @Author : lianxiujuan
# @File :
# @中文描述 :  容器取样，异常操作
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
    @pytest.mark.parametrize('numerror',['0.0000001','-2',' ','9999999999','JKJ','**'])
    def test_Container_Sample(self,numerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_sample(numerror,state)
        assert new_page_source('取样数量不能大于容器剩余量') or new_page_source('请输入精度为6位的非0小数')
        new_click(cancel)
        new_click(second_container)
        sleep(1)
