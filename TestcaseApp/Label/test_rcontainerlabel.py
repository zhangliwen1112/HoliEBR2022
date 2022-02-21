#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 标签-接收容器
"""

import pytest
import sys
from DataApp.LabelmgData import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.pageobjectAPP.pageLabel import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
import random,string

labeldata = ''.join(random.sample(string.ascii_letters + string.digits, 4))


class Test_rcontainerlabel:
    def setup_class(self):
        login_label()
        new_click(rcontainer)
        sleep(1)
        label_add(labeldata, labeldata, labeldata, labeldata)
        sleep(1)

    def teardown_class(self):
        Close_current_tab()

    # 新增 标签-接收容器
    def test_add_rcontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(rcontainercode, rcontainername, rcontainerdesc, rcontainerzpl)
        time.sleep(2)
        assert new_page_source(rcontainercode)

    # 搜索 标签-接收容器
    def test_search_rcontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", rcontainercode)
        time.sleep(2)
        ele = new_find_elements(searchresult)
        text = new_get_text_ele(ele[0])
        time.sleep(2)
        assert rcontainercode in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑 标签-接收容器
    def test_edit_rcontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(rcontainercode)
        label_edit(editname, editdesc, editzpl)
        time.sleep(2)
        assert new_page_source(editname)

    # 设置标准模板
    def test_setdefault_rcontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_setdefault()
        time.sleep(2)
        select_item(labeldata)
        label_setdefault()
        time.sleep(2)

    # 删除 标签-接收容器
    def test_delete_rcontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(rcontainercode)
        label_delete()
        time.sleep(2)
        assert new_page_source(rcontainercode) == False
        sleep(1)
