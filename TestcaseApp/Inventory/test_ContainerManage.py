# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 17:13 
# @Author : 张丽雯 
# @File : test_ContainerManagecase.py 
# @中文描述 :  容器管理界面
import sys
import pytest
from DataApp.ContainerManageData import *
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

    # 查看容器明细
    def test_Container_Manage_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_detail(isopen)

    # 移动容器库位
    def test_Container_Manage_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_move()

    # 返回容器库位
    def test_Container_Manage_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_reback()

    # 拆分容器 - 原托盘\新容器
    @pytest.mark.parametrize('type,num', [('原托盘', '0.001'), ('新容器', '0.002')])
    def test_Container_Manage_004(self, type, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_split(type, num)
        sleep(2)

    # 拆分容器 - 重新打印标签
    def test_Container_Manage_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_label(num)

    # 筛选锁定状态容器
    def test_Container_Manage_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_option('容器状态',search_status)
        sleep(1)
        assert new_page_source(search_status)

    # 容器状态--驳回
    def test_Container_Manage_007(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        container_status(reject_status)
        sleep(1)
        search_option('容器状态', '---请选择---')
        sleep(1)
        assert new_page_source(reject_status)

