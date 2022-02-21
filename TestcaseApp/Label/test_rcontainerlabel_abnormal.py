# -*- coding: utf-8 -*- 
# @Time : 2021/5/20 17:00 
# @Author : 张丽雯 
# @File : test_rcontainerlabel_abnormal.py 
# @中文描述 :  标签-接收容器，异常测试用例
import pytest
import sys
from DataApp.LabelmgData import *
from src.pageobjectAPP.pageLabel import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *


class Test_rcontainerlabel_Abnormal:
    def setup_class(self):
        login_label()
        new_click(rcontainer)
        sleep(2)
        label_add(code1, name1, desc1, zpl1)

    def teardown_class(self):
        select_item(code1)
        sleep(1)
        label_delete()
        sleep(1)
        Close_current_tab()

    @pytest.mark.parametrize('code, name, desc, zpl', code_abnormal_01)
    def test_rcontainerlabel_code_abnormal_001(self, code, name, desc, zpl):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(code, name, desc, zpl)
        assert is_text_present('编码为必填项')
        new_click(cancel_button)
        sleep(1)

    @pytest.mark.parametrize('code, name, desc, zpl', code_abnormal_02)
    def test_rcontainerlabel_code_abnormal_002(self, code, name, desc, zpl):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(code, name, desc, zpl)
        assert is_text_present('编码由字母、数字、/_-组成，不能以特殊字符开头')
        new_click(cancel_button)
        sleep(1)

    @pytest.mark.parametrize('code, name, desc, zpl', code_abnormal_03)
    def test_rcontainerlabel_code_abnormal_003(self, code, name, desc, zpl):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(code, name, desc, zpl)
        assert is_text_present('标签编码 ' + code + ' 已存在，请重新输入')
        new_click(cancel_button)
        sleep(1)

    @pytest.mark.parametrize('code, name, desc, zpl', name_abnormal_01)
    def test_rcontainerlabel_name_abnormal_001(self, code, name, desc, zpl):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(code, name, desc, zpl)
        assert is_text_present('名称为必填项')
        new_click(cancel_button)
        sleep(1)

    @pytest.mark.parametrize('code, name, desc, zpl', name_abnormal_02)
    def test_rcontainerlabel_name_abnormal_002(self, code, name, desc, zpl):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(code, name, desc, zpl)
        assert is_text_present('标签名称 ' + name + ' 已存在，请重新输入')
        new_click(cancel_button)
        sleep(1)

    @pytest.mark.parametrize('code, name, desc, zpl', zpl_abnormal)
    def test_rcontainerlabel_zpl_abnormal_001(self, code, name, desc, zpl):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(code, name, desc, zpl)
        assert is_text_present('ZPL为必填项')
        new_click(cancel_button)
        sleep(1)
