# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 13:45 
# @Author : 张丽雯 
# @File : test_weightcase.py 
# @中文描述 :  砝码配置
import sys
from DataApp.WeightData import *
from src.public.Logger import *
from src.pageobjectAPP.pageWeight import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import *


class Test_Weight:
    def setup_class(self):
        app_login(username, password)
        login_weight()

    #
    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增砝码配置
    # @pytest.mark.skip
    def test_add_weight(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_add(weightname1,add_value,add_unit)
        sleep(2)
        assert new_page_source(weightname1)

    # 筛选
    def test_search_weight(self):
        search_item('名称',weightname1)
        assert new_page_source(weightname1)

    #编辑砝码配置
    def test_edit_weight(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_edit(edit_value,edit_unit)
        sleep(2)
        assert edit_value in new_get_text("//div[@role='row' and @row-index='0']//div[@col-id='weight']")

    #删除砝码
    def test_delete_weight(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_delete()
        assert (is_text_present(edit_value), '删除失败！')

    # 清除筛选
    def test_search_clear(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', ' ')
        assert (is_text_present(weightname1), '删除失败！')


