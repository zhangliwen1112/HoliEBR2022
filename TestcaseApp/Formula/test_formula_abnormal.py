# -*- coding: utf-8 -*- 
# @Time : 2021/2/22 15:30 
# @Author : 张丽雯 
# @File : test_formula_abnormal.py 
# @中文描述 :  处方管理异常场景
import sys
import pytest
from DataApp.FormulaData import *
from src.pageobjectAPP.pageFormula import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.elements import alert_txt


class Test_Formula:
    def setup_class(self):
        sleep(2)
        login_formula()
        formula_add_web(add_name1, add_type1,add_num, r_unit, add_weight, w_unit)

    def teardown_class(self):
        Close_current_tab()

    # 新增处方_名称异常场景
    @pytest.mark.parametrize('formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit', abnormal_name)
    def test_add_abnormal_001(self, formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_add_web(formula_name, formula_type,reference_num, add_r_unit, equivalent_weight, add_w_unit)
        assert "请按照格式要求填写数据" in new_get_text(alert_txt)

    # 新增处方_参考数量异常场景
    @pytest.mark.parametrize('formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit', abnormal_num)
    def test_add_abnormal_002(self, formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_add_web(formula_name, formula_type,reference_num, add_r_unit, equivalent_weight, add_w_unit)
        assert "请按照格式要求填写数据" in new_get_text(alert_txt)

    # 新增处方_等价称量异常场景
    @pytest.mark.parametrize('formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit', abnormal_weight)
    def test_add_abnormal_003(self, formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_add_web(formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit)
        assert "请按照格式要求填写数据" in new_get_text(alert_txt)

    # 编辑处方_名称异常场景
    @pytest.mark.parametrize('formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit', abnormal_name)
    def test_edit_abnormal_001(self, formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_edit_web(formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit)
        assert "请按照格式要求填写数据" in new_get_text(alert_txt)

    # 编辑处方_参考数量异常场景
    @pytest.mark.parametrize('formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit', abnormal_num)
    def test_edit_abnormal_002(self, formula_name, formula_type,reference_num, add_r_unit, equivalent_weight, add_w_unit):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_edit_web(formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit)
        assert "请按照格式要求填写数据" in new_get_text(alert_txt)

    # 编辑处方_等价称量异常场景
    @pytest.mark.parametrize('formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit', abnormal_weight)
    def test_edit_abnormal_003(self, formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        formula_edit_web(formula_name,formula_type, reference_num, add_r_unit, equivalent_weight, add_w_unit)
        assert "请按照格式要求填写数据" in new_get_text(alert_txt)

