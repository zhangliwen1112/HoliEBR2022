# coding=utf-8

"""
Created on 2020/9/14
@author: zhangliwen
@desc:HoliEBR-Admin 工作中心
"""
import sys
import pytest
from src.pageobjectAdmin.pageWorkerCentre import *
from DataAdmin.WorkerCentreData import *
from src.public.Logger import Log
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *

class Test_WorkerCenter():

    # 进入工作中心页面
    def test_workercenter_manage(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sleep(3)
        login_worker_centre()


    # 新增工作中心
    def test_workercenter_add(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_add(add_code1, add_name1)
        sleep(1)
        worker_center_add(add_code2, add_name2)
        sleep(1)
        assert new_page_source(add_name1)

    # 筛选工作中心
    def test_workercenter_search(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',add_code1)
        sleep(1)
        assert new_page_source(add_name1)

    # 编辑新增工作中心
    def test_workercenter_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_edit(edit_name,'')
        sleep(1)
        assert new_page_source(edit_name)


    # 关联工作站
    def test_workercenter_relation(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_relation()

    # 去关联
    def test_workercenter_remove(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_remove()


    # 删除工作中心
    def test_workercenter_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        worker_center_delete()

    # 清除筛选条件
    def test_workercenter_search_cancel(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')
        sleep(2)
        new_click(Work_Centre)



