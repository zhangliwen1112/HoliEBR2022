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

weighcode = 'lian'

class Test_weighset:
    def setup_class(self):
        app_login(username, password)
        login_weighset()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 新增衡器，最小容量异常1
    @pytest.mark.parametrize('minvalueerror',[0,'2.3666','fds','&(*','-1',' '])
    def test_addweighset_minvalueerror1(self, minvalueerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(minvalueerror, addmaxvaluedata, addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为3位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，最小容量异常2
    def test_addweighset_minvalueerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(11111111111, addmaxvaluedata, addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，最大容量异常1
    @pytest.mark.parametrize('maxvalueerror',[0,'2.3666','fds','&(*','-1',' '])
    def test_addweighset_maxvalueerror1(self, maxvalueerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add('0.001', maxvalueerror, addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为3位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，最大容量异常2
    def test_addweighset_maxvalueerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add('0.001', '11111111111', addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，最大容量小于最小容量
    def test_addweighset_valueerror(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add('5', '3', addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入大于最小容量的数值')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，证书有效期异常
    def test_addweighset_certerror1(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata, '-1')
        time.sleep(2)
        assert new_page_source('请输入大于0的数值')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，证书有效期异常
    def test_addweighset_certerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata, '2.366')
        time.sleep(2)
        assert new_page_source('请输入整数')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，证书有效期异常
    def test_addweighset_certerror3(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata, ' ')
        time.sleep(2)
        assert new_page_source('请输入')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，偏差异常1
    @pytest.mark.parametrize('offseterror', [0, '2.3666445', 'fds', '&(*', '-1',' '])
    def test_addweighset_offseterror1(self, offseterror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, offseterror, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为6位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，偏差异常2
    def test_addweighset_offseterror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, '11111111111', addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，校准公差异常1
    @pytest.mark.parametrize('calerror', [0, '2.3666445', 'fds', '&(*', '-1',' '])
    def test_addweighset_calerror1(self, calerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, addoffsetdata, calerror, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为6位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 新增衡器，校准公差异常2
    def test_addweighset_calerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weighset_withcert_add(addminvaluedata, addmaxvaluedata, addoffsetdata, '11111111111', addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，最小容量异常1
    @pytest.mark.parametrize('minvalueerror',[0,'2.3666','fds','&(*','-1',' '])
    def test_editweighset_minvalueerror1(self, minvalueerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(minvalueerror, addmaxvaluedata, addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为3位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，最小容量异常2
    def test_editweighset_minvalueerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(11111111111, addmaxvaluedata, addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，最大容量异常1
    @pytest.mark.parametrize('maxvalueerror',[0,'2.3666','fds','&(*','-1',' '])
    def test_editweighset_maxvalueerror1(self, maxvalueerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit('0.001', maxvalueerror, addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为3位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，最大容量异常2
    def test_editweighset_maxvalueerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit('0.001', '11111111111', addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，最大容量小于最小容量
    def test_editweighset_valueerror(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit('5', '3', addoffsetdata, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入大于最小容量的数值')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，证书有效期异常
    def test_editweighset_certerror1(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata, '-1')
        time.sleep(2)
        assert new_page_source('请输入大于0的数值')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，证书有效期异常
    def test_editweighset_certerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata, '2.366')
        time.sleep(2)
        assert new_page_source('请输入整数')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，证书有效期异常
    def test_editweighset_certerror3(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, addoffsetdata, addcalerrordata, ' ')
        time.sleep(2)
        assert new_page_source('请输入')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，偏差异常1
    @pytest.mark.parametrize('offseterror', [0, '2.3666445', 'fds', '&(*', '-1',' '])
    def test_editweighset_offseterror1(self, offseterror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, offseterror, addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为6位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，偏差异常2
    def test_editweighset_offseterror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, '11111111111', addcalerrordata, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，校准公差异常1
    @pytest.mark.parametrize('calerror', [0, '2.3666445', 'fds', '&(*', '-1',' '])
    def test_editweighset_calerror1(self, calerror):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, addoffsetdata, calerror, addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入精度为6位的非0小数')
        new_click(cancel_button)
        sleep(1)

    # 编辑衡器，校准公差异常2
    def test_editweighset_calerror2(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(weighcode)
        weighset_edit(addminvaluedata, addmaxvaluedata, addoffsetdata, '11111111111', addcertdaysdata)
        time.sleep(2)
        assert new_page_source('请输入小于9999999999的数值')
        new_click(cancel_button)
        sleep(1)
