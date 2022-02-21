# -*- coding: utf-8 -*-
# @Time : 2021/1/10 15:30
# @Author : 张丽雯
# @File : test_formula.py
# @中文描述 :  处方管理
import sys
import pytest
from DataApp.FormulaData import *
from src.pageobjectAPP.pageFormula import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import search_item
from src.public.common.elements import alert_txt


class Test_Formula:
    def setup_class(self):
        login_formula()

    def teardown_class(self):
        Close_current_tab()

    # 新增处方-测试/研发类型的处方
    # @pytest.mark.skip
    def test_formula_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_add_web(add_name1,add_type1, add_num, r_unit, add_weight, w_unit)
        assert new_page_source(add_name1)

    # 筛选数据
    def test_formula_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', add_name1)
        assert new_page_source(add_name1)

    # 编辑处方
    # @pytest.mark.skip
    def test_formula_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_edit_web(edit_name, edit_num, edit_r_unit, edit_weight, edit_w_unit)
        assert new_page_source(edit_name)


    # 新增处方物料
    @pytest.mark.parametrize('num',['20','2500'])
    def test_formula_004(self, num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_add_material_001(num,m_unit)
        assert "保存成功" in new_get_text(alert_txt)

    # 删除处方物料
    def test_formula_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_delete_material()

    # 提交处方
    def test_formula_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_submit()
        sleep(2)
        assert '已提交' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')

    # 批准处方
    def test_formula_007(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_approve()
        sleep(2)
        assert '已批准' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')

    # 清除筛选条件
    def test_formula_008(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('名称', ' ')
        sleep(2)
        assert '已批准' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')

    # 修订处方
    def test_formula_009(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_revise()
        sleep(2)
        assert '1' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="version"]')

    # 失效处方
    def test_formula_010(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_noeffect()
        sleep(2)
        assert '已失效' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')

    # 复制处方
    def test_formula_011(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_copy_formula()
        sleep(2)
        assert '可编辑' in new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="status"]')

    # 新增处方-最大编码数验证，其中编码规则是2位数，最大应为99
    @pytest.mark.skip
    def test_formula_012(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        code = new_get_text('//div[@role="row" and @row-index="0"]//div[@col-id="code"]')
        n = int(code[-2:])
        for i in range(n+1,100):
            formula_add_web(add_name1,add_type1, add_num, r_unit, add_weight, w_unit)


    # 新增生产/临床类型的处方
    @pytest.mark.parametrize('num',['20'])
    def test_formula_013(self,num):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_add_web(add_name2,add_type2, add_num, r_unit, add_weight, w_unit)
        assert new_page_source(add_name2)
        sleep(1)
        search_item('名称', add_name2)
        sleep(1)
        formula_add_material_001(num, m_unit)
        sleep(1)
        formula_submit()
        sleep(1)
        formula_approve()
        sleep(1)
        formula_verify()
        sleep(1)


