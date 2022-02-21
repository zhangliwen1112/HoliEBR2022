#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 衡器设置
"""

import pytest
import sys
from DataApp.WeighsetData import *
from src.pageobjectAPP.pageWeighset import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
from src.public.common.Close_current_tab import *

weighcode = 'abcde'

class Test_weighset:
    def setup_class(self):
        app_login(username, password)
        login_weighset()

    # def teardown_class(self):
    #     Close_current_tab()
    #     app_logout()

    # 新增衡器
    def test_add_weighset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_nocert_add(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata)
        time.sleep(2)
        assert new_page_source(weighcode)

    # 搜索衡器
    def test_search_weighset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", weighcode)
        time.sleep(2)
        text = new_get_text(firstdata_app)
        time.sleep(2)
        assert weighcode in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑衡器
    def test_edit_weighset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(editminvaluedata, editmaxvaluedata, editoffsetdata, editcalerrordata)
        time.sleep(2)
        assert new_page_source(editmaxvaluedata)

    # 删除衡器
    def test_delete_weighset(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_delete()
        time.sleep(2)
        assert new_page_source(weighcode) == False
