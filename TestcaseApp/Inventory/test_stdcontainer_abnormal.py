# -*- coding: utf-8 -*- 
# @Time : 2021/4/20 16:53 
# @Author : 张丽雯 
# @File : test_stdcontainer_abnormal.py 
# @中文描述 :  标准容器-异常场景用例
import sys
import pytest
from DataApp.stdcontainerData import *
from src.pageobjectAPP.pageStdcontainer import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Login import *
from src.public.common.Search_Item import search_item


class Test_StandardContainer:
    def setup_class(self):
        app_login(username, password)
        login_standard_container()
        add_standard_container(add_name1, add_tare)
        sleep(1)
        search_item('名称', add_name1)
        sleep(1)

    def teardown_class(self):
        delete_standard_container()
        sleep(1)
        Close_current_tab()
        app_logout()

    # 新增标准容器-名称以特殊字符开头
    def test_container_add_abmoral_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container('-112', add_tare)
        sleep(1)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancle)

    # 新增标准容器-名称含有特殊字符
    def test_container_add_abmoral_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container('container@qw', add_tare)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancle)

    # 新增标准容器-名称为空
    def test_container_add_abmoral_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(' ', add_tare)
        assert is_text_present('请输入')
        new_click(cancle)

    # 新增标准容器-名称超过最大字符
    def test_container_add_abmoral_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(
            '12sgdhsgsdggggggggg12sgdhsgsdggggggggggcontaineqgcontainer001ASAD12sgdhsgsdggggggggggcontainer001ASAD',
            add_tare)
        assert is_text_present('请输入1到100个字符')
        new_click(cancle)

    # 新增标准容器-平均质量为空
    def test_container_add_abmoral_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, ' ')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 新增标准容器-平均质量超过最大值
    def test_container_add_abmoral_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, '10000000000')
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 新增标准容器-平均质量小数位数超过3位
    def test_container_add_abmoral_007(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, '10.1234')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 新增标准容器-平均质量为负数
    def test_container_add_abmoral_008(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, '-4')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 新增标准容器-高为空
    def test_container_add_abmoral_009(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, ' ')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-高超过最大值
    def test_container_add_abmoral_010(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, '1000')
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 新增标准容器-高小数位数超过3位
    def test_container_add_abmoral_011(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, '10.1')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-高为负数
    def test_container_add_abmoral_012(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, '-4')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-长为空
    def test_container_add_abmoral_013(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, ' ')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-长超过最大值
    def test_container_add_abmoral_014(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, '1000')
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 新增标准容器-长小数位数超过3位
    def test_container_add_abmoral_015(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, '10.1')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-长为负数
    def test_container_add_abmoral_016(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, '-4')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-宽为空
    def test_container_add_abmoral_017(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, ' ')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-宽超过最大值
    def test_container_add_abmoral_018(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, '1000')
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 新增标准容器-宽小数位数超过3位
    def test_container_add_abmoral_019(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, '10.1')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-宽为负数
    def test_container_add_abmoral_020(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, '-4')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准容器-比例为空
    def test_container_add_abmoral_021(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, add_w, ' ')
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 新增标准容器-比例超过最大值
    def test_container_add_abmoral_022(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, add_w, '10000000000')
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 新增标准容器-比例超过最大值
    def test_container_add_abmoral_023(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, add_w, '10.urllib3介绍')
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 新增标准容器-比例超过最大值
    def test_container_add_abmoral_024(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, add_tare, add_qty, add_h, add_l, add_w, '-1')
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 新增标准容器-皮重为空
    def test_container_add_abmoral_025(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name,  ' ')
        assert is_text_present('请输入')
        new_click(cancle)

    # 新增标准容器-皮重超过最大值
    def test_container_add_abmoral_026(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, '10000000000')
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 新增标准容器-皮重小数位数超过3位
    def test_container_add_abmoral_027(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, '1.1234')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 新增标准容器-皮重为负
    def test_container_add_abmoral_028(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        add_standard_container(add_name, '-1')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑容器-名称含有特殊字符
    def test_container_edit_adnomal_001(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container('-112', edit_tare)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancle)

    # 编辑标准容器-名称含有特殊字符
    def test_container_edit_adnomal_002(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container('container@qw', edit_tare)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancle)

    # 编辑标准容器-名称为空
    def test_container_edit_adnomal_003(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(' ', edit_tare)
        assert is_text_present('请输入')
        new_click(cancle)

    # 编辑标准容器-名称超过最大字符
    def test_container_edit_adnomal_004(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(
            '12sgdhsgsdggggggggg12sgdhsgsdggggggggggcontaineqgcontainer001ASAD12sgdhsgsdggggggggggcontainer001ASAD',
            edit_tare)
        assert is_text_present('请输入1到100个字符')
        new_click(cancle)

    # 编辑标准容器-平均质量为空
    def test_container_edit_abmoral_005(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, ' ')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑标准容器-平均质量超过最大值
    def test_container_edit_abmoral_006(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, '10000000000')
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 编辑标准容器-平均质量小数位数超过3位
    def test_container_edit_abmoral_007(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, '10.1234')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑标准容器-平均质量为负数
    def test_container_edit_abmoral_008(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, '-4')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑标准容器-高为空
    def test_container_edit_abmoral_009(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, ' ')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-高超过最大值
    def test_container_edit_abmoral_010(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, '1000')
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 编辑标准容器-高小数位数超过3位
    def test_container_edit_abmoral_011(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, '10.1')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-高为负数
    def test_container_edit_abmoral_012(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, '-4')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-长为空
    def test_container_edit_abmoral_013(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, ' ')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-长超过最大值
    def test_container_edit_abmoral_014(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, '1000')
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 编辑标准容器-长小数位数超过3位
    def test_container_edit_abmoral_015(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, '10.1')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-长为负数
    def test_container_edit_abmoral_016(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, '-4')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-宽为空
    def test_container_edit_abmoral_017(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, ' ')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-宽超过最大值
    def test_container_edit_abmoral_018(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, '1000')
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 编辑标准容器-宽小数位数超过3位
    def test_container_edit_abmoral_019(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, '10.1')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-宽为负数
    def test_container_edit_abmoral_020(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, '-4')
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准容器-比例为空
    def test_container_edit_abmoral_021(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, add_w, ' ')
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 编辑标准容器-比例超过最大值
    def test_container_edit_abmoral_022(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, add_w, '10000000000')
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 编辑标准容器-比例超过最大值
    def test_container_edit_abmoral_023(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, add_w, '10.urllib3介绍')
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 编辑标准容器-比例超过最大值
    def test_container_edit_abmoral_024(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, edit_tare, add_qty, add_h, add_l, add_w, '-1')
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 编辑标准容器-皮重为空
    def test_container_edit_abmoral_025(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, ' ')
        assert is_text_present('请输入')
        new_click(cancle)

    # 编辑标准容器-皮重超过最大值
    def test_container_edit_abmoral_026(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, '10000000000')
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 编辑标准容器-皮重小数位数超过3位
    def test_container_edit_abmoral_027(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, '1.1234')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑标准容器-皮重为负
    def test_container_edit_abmoral_028(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        edit_standard_container(edit_name, '-1')
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)
