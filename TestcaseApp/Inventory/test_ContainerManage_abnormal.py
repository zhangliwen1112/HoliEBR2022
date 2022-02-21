# -*- coding: utf-8 -*- 
# @Time : 2021/4/22 11:44 
# @Author : 张丽雯 
# @File : test_ContainerManage_abnormal.py 
# @中文描述 :  容器管理异常场景用例
import sys
import pytest
from src.pageobjectAPP.pageContainerManage import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_ContainerManage:
    def setup_class(self):
        app_login(username, password)
        login_container_manage()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 拆分容器 - 原托盘\新容器--拆分数量小数位数不满足，拆分数量为负
    @pytest.mark.parametrize('type,num',
                             [('原托盘', '0.1234567'), ('原托盘', '-1'), ('新容器', '-2.3'), ('新容器', '0.0000001'), ])
    def test_Container_Manage_001(self, type, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_split(type, num)
        sleep(2)
        assert is_text_present('请输入精度为6位的非0小数')
        new_click(cancel)

    # 拆分容器 - 原托盘\新容器-拆分数量过大
    @pytest.mark.parametrize('type,num', [('原托盘', '999999999'), ('新容器', '999999999')])
    def test_Container_Manage_002(self, type, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_split(type, num)
        sleep(2)
        assert is_text_present('拆分数量不能大于容器剩余量')
        new_click(cancel)

    # 拆分容器 - 原托盘\新容器--拆分数量为空
    @pytest.mark.parametrize('type,num', [('原托盘', ''), ('新容器', '')])
    def test_Container_Manage_003(self, type, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_split(type, num)
        sleep(2)
        assert is_text_present('请输入')
        new_click(cancel)
