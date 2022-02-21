# coding=utf-8

"""
Created on 2020/9/14
@author: zhangliwen
@desc:HoliEBR-Admin 位置管理页面
"""
import sys
import pytest
from src.pageobjectAdmin.pageLocationManage import *
from DataAdmin.LocationManageData import *
from src.public.Logger import Log
from src.public.common.Search_Item import *

class Test_Location_Manage:

    # 进入工厂模型-位置管理页面
    def test_location_manage(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_Location_Manage()
        sleep(1)

    # 新增位置
    @pytest.mark.parametrize(('code','name'),add_data1)
    def test_location_add(self,code,name):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_add(code,name)
        assert new_page_source(name01)

    # 筛选
    def test_location_search(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',code01)
        sleep(2)
        assert new_page_source(name01)

    # 编辑位置
    def test_location_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_edit('xiugai')
        assert new_page_source('xiugai')


    # 删除位置
    def test_location_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Location_Manage_delete()

    # 清除筛选条件
    def test_section_search_clear(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')
        new_click(Factory_Mode)
        sleep(1)