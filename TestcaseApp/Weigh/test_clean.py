# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 11:01 
# @Author : 张丽雯 
# @File : test_cleancase.py 
# @中文描述 :  清洁配置用例
import sys
import pytest
from DataApp.CleanData import *
from src.public.Logger import *
from src.pageobjectAPP.pageClean import *
from src.public.common.Close_current_tab import Close_current_tab


class Test_Clean:
    def test_clean_login(self):
        login_clean()
        assert new_page_source('清洁配置')

    # 新增清洁配置
    # @pytest.mark.skip
    def test_add_clean(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        clean_add(add_code1,name,ruletype)
        assert name in new_get_text('//div[@role="row" and @row-index="0"]//div[contains(.,"clean")]')

    #筛选
    def test_search_clean(self):
        clean_search_web(text)
        assert new_page_source(text)

    #编辑清洁配置
    def test_edit_clean(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        clean_edit('xiugai','物料')
        assert 'xiugai' in new_get_text('//div[@role="row" and @row-index="0"]//div[contains(.,"xiugai")]')

    # 删除清洁配置
    def test_delete_clean(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        clean_delete()
        assert (is_text_present('xiugai'),'删除失败！')
        Close_current_tab()
