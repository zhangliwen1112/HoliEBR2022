#coding=utf-8

"""
Created on 2020/9/14
@author: lianxiujuan
@desc: 工单管理
"""


import pytest
import sys
from DataApp.WorkorderData import *
from src.public.common.Close_current_tab import *
from src.public.common.Login import *
from src.pageobjectAPP.pageWorkorder import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *



class Test_workordermg:
    def setup_class(self):
        app_login(username, password)
        login_wo()


    # def teardown_class(self):
    #     Close_current_tab()
    #     app_logout()

    # 新增工单
    def test_add_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_add()
        assert "生产工单" in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="orderType.name"]')


    # 搜索工单
    def test_search_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        search_item('编码', wo_code)
        time.sleep(2)
        assert new_page_source(wo_code)
        search_item('编码', ' ')


    # 编辑工单
    def test_edit_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        time.sleep(2)
        select_item(wo_code)
        wo_edit(editqtydata)
        time.sleep(2)


    # 复制工单
    def test_copy_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        time.sleep(2)
        select_item(wo_code)
        wo_copy()
        time.sleep(3)
        copy_code = new_get_text(firstdata_app)
        time.sleep(2)
        assert int((wo_code.split('WO'))[1]) + 1 == int((copy_code.split('WO'))[1])


    # 发布工单、取消发布工单
    def test_release_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        time.sleep(2)
        select_item(wo_code)
        wo_release()
        search_item('编码', wo_code)
        time.sleep(2)
        assert new_page_source("已发布")
        select_item(wo_code)
        wo_cancelre()
        time.sleep(2)
        assert new_page_source("可编辑的")
        time.sleep(1)
        search_item('编码', ' ')


    # 修订工单
    def test_mod_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        time.sleep(2)
        select_item(wo_code)
        wo_mod(modqtydata)
        time.sleep(2)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="3"]') == '1'


    # 取消工单
    def test_cancel_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        time.sleep(2)
        select_item(wo_code)
        wo_cancel()
        time.sleep(2)
        assert new_page_source(wo_code) == False


    # 终止工单、关闭工单
    def test_stop_wo(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        wo_code = wo_add()
        time.sleep(2)
        select_item(wo_code)
        wo_release()
        time.sleep(2)
        select_item(wo_code)
        wo_stop()
        search_item('编码', wo_code)
        time.sleep(2)
        assert new_page_source("生产终止")
        select_item(wo_code)
        wo_close()
        time.sleep(2)
        assert new_page_source("已关闭")
        search_item('编码', ' ')


    # 修订工单-验证修订工单的最大版本号为99
    def test_mod_wo_max(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        version = new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="version"]')
        n = int(version)
        for i in range(n+1,100):
            wo_mod(modqtydata)
            sleep(1)



if __name__ == '__main__':
    pytest.main(['-s','test_workorder.py'])
