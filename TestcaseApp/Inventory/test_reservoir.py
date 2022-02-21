# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 15:09 
# @Author : 张丽雯 
# @File : test_reservoircase.py
# @中文描述 :  库区管理
import sys

import pytest
from DataApp.KuquData import *
from src.pageobjectAPP.pageStolocation import *
from src.public.Logger import *
from src.pageobjectAPP.pageReservoir import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import search_item


class Test_Reservoir:
    def setup_class(self):
        app_login(username, password)
        # login_stolocation()
        # stolocation_add(kuwei_code,kuwei_name)
        # Close_current_tab()
    #
    def teardown_class(self):
        # Close_current_tab()
        # login_stolocation()
        # search_item('编码',kuwei_code)
        # stolocation_delete()
        # search_item('编码',' ')
        # sleep(1)
        Close_current_tab()
        app_logout()

    # 新增库区
    def test_reservoir_add(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_reservoir()
        kuqu_add(kuqu_code,kuqu_name)
        assert is_text_present(kuqu_name)


    #筛选
    def test_reservoir_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',kuqu_code)
        sleep(1)
        assert is_text_present(kuqu_code)


    #编辑库区
    def test_reservoir_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_edit(kuqu_editname)
        assert is_text_present(kuqu_editname)

    #关联库位
    def test_reservoir_relation(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_relation_kuwei()

    # 去关联库位
    # @pytest.mark.skip
    def test_reservoir_remove(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_remove_kuwei()

    # 删除库区
    def test_reservoir_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        kuqu_delete()
        sleep(1)
        assert (is_text_present(kuqu_editname),'删除成功！')

    # 删除库区
    def test_reservoir_search_clear(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')
        assert (is_text_present(kuqu_editname),'显示正确！')
