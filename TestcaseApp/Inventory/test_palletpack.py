# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 18:08 
# @Author : 张丽雯 
# @File : test_palletpackcase.py 
# @中文描述 :  托盘包装方式
import sys

import pytest
from DataApp.PalletpackData import *
from src.public.Logger import *
from src.pageobjectAPP.pagePalletpack import *
from src.public.common.Close_current_tab import *
from src.public.common.Search_Item import search_item


class Test_Pallet_Pack:
    def setup_class(self):
        app_login(username, password)
        login_pallet_pack()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增托盘包装方式
    def test_pallet_pack_add(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_pallet_pack(volume,mater)
        sleep(1)
        assert new_page_source(mater)

    # 筛选
    def test_pallet_pack_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('物料编码',mater)
        sleep(1)
        assert new_page_source(mater)

    # 编辑包装方式
    def test_pallet_pack_edit(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_pallet_pack('3')
        sleep(1)
        assert new_page_source(mater)

    # 删除
    def test_pallet_pack_delete(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        delete_pallet_pack()
        sleep(1)
        assert (is_text_present(mater),'删除失败！')

    # 清除筛选
    def test_pallet_pack_search_clear(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('物料编码',' ')
        sleep(1)
        assert (is_text_present(mater),'不存在！')
