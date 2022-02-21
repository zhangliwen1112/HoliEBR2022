# -*- coding: utf-8 -*- 
# @Time : 2021/4/21 10:33 
# @Author : 张丽雯 
# @File : test_Stdpallet_abnormal.py 
# @中文描述 :  标准托盘异常场景用例
import pytest
import sys
from DataApp.StdpalletData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageStdpallet import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
from ElementApp.PalletPackPaga import *


class Test_stdpallet:
    def setup_class(self):
        app_login(username, password)
        login_stdpallet()
        stdpallet_add(addnamedata, addtaredata,addweightdata, addheightdata,addlongthdata, addwidthdata, addratiodata)
        sleep(1)
        search_item("名称", addnamedata)
        sleep(1)

    def teardown_class(self):
        stdpallet_delete()
        app_logout()

    # 新增标准托盘-名称有特殊字符
    @pytest.mark.parametrize('name,tare',name_list1)
    def test_add_name_abnormal_001(self,name,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancle)

    # 新增标准托盘-名称为空
    @pytest.mark.parametrize('name,tare',name_list2)
    def test_add_name_abnormal_002(self,name,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare)
        assert is_text_present('请输入')
        new_click(cancle)

    # 新增标准托盘-名称超过最大字符
    @pytest.mark.parametrize('name,tare',name_list3)
    def test_add_name_abnormal_003(self,name,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare)
        assert is_text_present('请输入1到100个字符')
        new_click(cancle)

    # 新增标准托盘-平均质量超过最大字符
    @pytest.mark.parametrize('name,tare,qty', qty_list1)
    def test_add_qty_abnormal_001(self, name, tare,qty):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name, tare,qty)
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 新增标准托盘-平均质量为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty', qty_list2)
    def test_add_qty_abnormal_002(self, name, tare,qty):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty)
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 新增标准托盘-H超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high', high_list1)
    def test_add_high_abnormal_001(self, name, tare,qty,high):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high)
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 新增标准托盘-h为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty,high', high_list2)
    def test_add_high_abnormal_002(self, name, tare,qty,high):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high)
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准托盘-L超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high,long', long_list1)
    def test_add_long_abnormal_001(self, name, tare,qty,high,long):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high,long)
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 新增标准托盘-L为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty,high,long', long_list2)
    def test_add_long_abnormal_002(self, name, tare,qty,high,long):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high,long)
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准托盘-W超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high,long,width', width_list1)
    def test_add_width_abnormal_001(self, name, tare,qty,high,long,width):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high,long,width)
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 新增标准托盘-W为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty,high,long,width', width_list2)
    def test_add_width_abnormal_002(self, name, tare,qty,high,long,width):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high,long,width)
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 新增标准托盘-比例超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high,long,width,ratio', ratio_list1)
    def test_add_ratio_abnormal_001(self, name, tare,qty,high,long,width,ratio):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high,long,width,ratio)
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 新增标准托盘-比例为空、小数位数超过2位、为负
    @pytest.mark.parametrize('name,tare,qty,high,long,width,ratio', ratio_list2)
    def test_add_ratio_abnormal_002(self, name, tare,qty,high,long,width,ratio):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare,qty,high,long,width,ratio)
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 新增标准托盘-皮重超过最大值
    @pytest.mark.parametrize('name,tare', tare_list1)
    def test_add_tare_abnormal_001(self, name, tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name,tare)
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 新增标准托盘-皮重为空
    @pytest.mark.parametrize('name,tare', tare_list2)
    def test_add_tare_abnormal_002(self, name, tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name, tare)
        assert is_text_present('请输入')
        new_click(cancle)

    # 新增标准托盘-皮重小数位数不满足，或为负
    @pytest.mark.parametrize('name,tare', tare_list3)
    def test_add_tare_abnormal_003(self, name, tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_add(name, tare)
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑标准托盘-名称有特殊字符
    @pytest.mark.parametrize('name,tare',name_list1)
    def test_edit_name_abnormal_001(self,name,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare)
        assert is_text_present('名称由字母、数字、汉字、/_-组成，不能以特殊字符开头')
        new_click(cancle)

    # 编辑标准托盘-名称为空
    @pytest.mark.parametrize('name,tare',name_list2)
    def test_edit_name_abnormal_002(self,name,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare)
        assert is_text_present('请输入')
        new_click(cancle)

    # 编辑标准托盘-名称超过最大字符
    @pytest.mark.parametrize('name,tare',name_list3)
    def test_edit_name_abnormal_003(self,name,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare)
        assert is_text_present('请输入1到100个字符')
        new_click(cancle)

    # 编辑标准托盘-平均质量超过最大字符
    @pytest.mark.parametrize('name,tare,qty', qty_list1)
    def test_edit_qty_abnormal_001(self, name, tare,qty):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name, tare,qty)
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 编辑标准托盘-平均质量为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty', qty_list2)
    def test_edit_qty_abnormal_002(self, name, tare,qty):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty)
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)

    # 编辑标准托盘-H超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high', high_list1)
    def test_edit_high_abnormal_001(self, name, tare,qty,high):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high)
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 编辑标准托盘-h为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty,high', high_list2)
    def test_edit_high_abnormal_002(self, name, tare,qty,high):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high)
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准托盘-L超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high,long', long_list1)
    def test_edit_long_abnormal_001(self, name, tare,qty,high,long):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high,long)
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 编辑标准托盘-L为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty,high,long', long_list2)
    def test_edit_long_abnormal_002(self, name, tare,qty,high,long):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high,long)
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准托盘-W超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high,long,width', width_list1)
    def test_edit_width_abnormal_001(self, name, tare,qty,high,long,width):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high,long,width)
        assert is_text_present('请输入小于等于999的数值')
        new_click(cancle)

    # 编辑标准托盘-W为空、小数位数超过4位、为负
    @pytest.mark.parametrize('name,tare,qty,high,long,width', width_list2)
    def test_edit_width_abnormal_002(self, name, tare,qty,high,long,width):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high,long,width)
        assert is_text_present('请输入大于0的整数')
        new_click(cancle)

    # 编辑标准托盘-比例超过最大字符
    @pytest.mark.parametrize('name,tare,qty,high,long,width,ratio', ratio_list1)
    def test_edit_ratio_abnormal_001(self, name, tare,qty,high,long,width,ratio):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high,long,width,ratio)
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 编辑标准托盘-比例为空、小数位数超过2位、为负
    @pytest.mark.parametrize('name,tare,qty,high,long,width,ratio', ratio_list2)
    def test_edit_ratio_abnormal_002(self, name, tare,qty,high,long,width,ratio):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name,tare,qty,high,long,width,ratio)
        assert is_text_present('请输入精度为2位的非0小数')
        new_click(cancle)

    # 编辑标准托盘-皮重超过最大值
    @pytest.mark.parametrize('name,tare', tare_list1)
    def test_edit_tare_abnormal_001(self, name, tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name, tare)
        assert is_text_present('请输入小于9999999999的数值')
        new_click(cancle)

    # 编辑标准托盘-皮重为空
    @pytest.mark.parametrize('name,tare', tare_list2)
    def test_edit_tare_abnormal_002(self, name, tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name, tare)
        assert is_text_present('请输入')
        new_click(cancle)

    # 编辑标准托盘-皮重小数位数不满足，或为负
    @pytest.mark.parametrize('name,tare', tare_list3)
    def test_edit_tare_abnormal_003(self, name, tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        stdpallet_edit(name, tare)
        assert is_text_present('请输入精度为3位的非0小数')
        new_click(cancle)