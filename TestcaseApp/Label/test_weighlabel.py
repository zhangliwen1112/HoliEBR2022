# coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 标签-称量
"""

import pytest
import sys
from DataApp.LabelmgData import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.pageobjectAPP.pageLabel import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
import random, string

labeldata = ''.join(random.sample(string.ascii_letters + string.digits, 4))


class Test_weighlabel:
    def setup_class(self):
        login_label()
        new_click(weigh)
        time.sleep(2)
        label_add(labeldata, labeldata, labeldata, labeldata)

    def teardown_class(self):
        Close_current_tab()

    # 新增 标签-称量
    def test_add_weighlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(weighcode, weighname, weighdesc, weighzpl)
        time.sleep(2)
        assert new_page_source(weighcode)

    # 搜索 标签-称量
    def test_search_weighlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", weighcode)
        time.sleep(2)
        ele = new_find_elements(searchresult)
        text = new_get_text_ele(ele[0])
        time.sleep(2)
        assert weighcode in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑 标签-称量
    def test_edit_weighlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        label_edit(editname, editdesc, editzpl)
        time.sleep(2)
        assert new_page_source(editname)

    # 设置标准模板
    def test_setdefault_weighlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_setdefault()
        time.sleep(2)
        select_item(labeldata)
        label_setdefault()
        time.sleep(2)

    # 删除 标签-称量
    def test_delete_weighlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        label_delete()
        time.sleep(2)
        assert (is_text_present(weighcode),'删除失败！')
        sleep(1)
