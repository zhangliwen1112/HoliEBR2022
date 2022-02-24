# -*- coding: utf-8 -*- 
# @Time : 2021/1/26 10:43 
# @Author : 张丽雯 
# @File : test_MIimport.py 
# @中文描述 :  MI新增、导入、批准、发布

import pytest
import sys
from src.pageobjectAdmin.pageMImanage import *
from DataAdmin.MIData import *
from src.public.common.Login import *
from src.public.common.Search_Item import *


class Test_MImanage:
    def setup_class(self):
        sleep(2)
        login_mimanage()
        sleep(2)

    # 新增MI
    def test_mimanage_add(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        mimanage_add(add_code1)
        sleep(2)
        assert new_page_source(add_code1)

    # 筛选MI
    def test_mimanage_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('MI编码', add_code1)
        sleep(2)
        assert new_page_source(add_code1)

    # 导入
    def test_mimanage_import(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        mimanage_design_into()
        mimanage_design_import('flows.json')
        sleep(4)
        mimanage_design_delete_tab()
        mimanage_design_close()

    # MI 批准
    def test_mimanage_approve(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        mimanage_approve()
        sleep(2)
        assert '已批准' in new_get_text("//div[@role='row' and @row-index='0']//span[@aria-colindex='6']")

    # MI 发布
    def test_mimanage_publish(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        mimanage_publish()
        sleep(2)
        assert '已发布' in new_get_text("//div[@role='row' and @row-index='0']//span[@aria-colindex='6']")
        search_item('MI编码', ' ')
        sleep(1)
        new_click(promg)
