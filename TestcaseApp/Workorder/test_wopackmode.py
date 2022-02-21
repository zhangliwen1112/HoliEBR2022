# -*- coding: utf-8 -*- 
# @Time : 2021/1/7 17:52 
# @Author : 张丽雯 
# @File : test_workpackmode.py 
# @中文描述 :  产品包装方式
import sys
import pytest
from src.public.Logger import *
from src.pageobjectAPP.pageWorkpackmode import *
from DataApp.WopackmodeData import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import *


class Test_workpack_mode:
    def setup_class(self):
        app_login(username, password)
        login_workpack_mode()

    #
    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增产品包装方式-默认包装
    @pytest.mark.a
    def test_workpack_mode_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_workpack_mode(packname1,isdefault1,Ptare,unit,Ctare,num)
        sleep(1)
        assert new_page_source(packname1)

    # 新增产品包装方式-非默认包装
    def test_workpack_mode_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_workpack_mode(packname2, isdefault2, Ptare, unit, Ctare, num)
        sleep(1)
        assert new_page_source(packname2)

    # 按包装说明筛选
    def test_workpack_mode_003(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('包装说明',packname1)
        sleep(2)
        assert new_page_source(packname1)

    # 编辑产品包装方式(原产品包装方式为默认，修改为非默认)
    def test_workpack_mode_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_workpack_mode(Ptare_edit, Ctare_edit, num_edit)
        assert 'N' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="isDefault"]')

    # 删除产品包装方式
    #@pytest.mark.skip
    def test_workpack_mode_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        delete_workpack_mode()
        assert (is_text_present(packname1), '删除失败！')

    #清除已有的筛选条件
    def test_workpack_mode_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('包装说明',' ')
        sleep(1)
        assert new_page_source(packname2)
