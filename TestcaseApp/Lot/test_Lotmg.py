#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 批次管理
"""

import pytest
import sys
from DataApp.LotMgData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageLotmg import *
from src.public.common.Select_Item import *
from src.pageobjectAPP.pageLotreceive import *
from src.public.common.Close_current_tab import *



class Test_lotmg:
    def setup_class(self):
        app_login(username, password)

    # def teardown_class(self):
    #     app_logout()

    # 批次维护
    def test_maint_lot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_lotreceive()
        lotno = lot2_add('1234', '1', '1')
        time.sleep(2)
        Close_current_tab()
        time.sleep(2)
        login_lotmg()
        time.sleep(4)
        select_item(lotno)
        lot_maint(analysisnoData, densityData, potencyData)
        time.sleep(2)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="6"]') == "带条件批准"
        Close_current_tab()
        time.sleep(3)

    # 锁定批次
    def test_locklot_lot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_lotreceive()
        lotno = lot2_add('1234', '1', '1')
        time.sleep(2)
        Close_current_tab()
        time.sleep(2)
        login_lotmg()
        time.sleep(4)
        select_item(lotno)
        lot_locklot()
        time.sleep(2)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="6"]') == "锁定"
        Close_current_tab()
        time.sleep(3)

    # 驳回批次
    def test_rejectlot_lot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_lotreceive()
        lotno = lot2_add('1234', '1', '1')
        time.sleep(2)
        Close_current_tab()
        time.sleep(2)
        login_lotmg()
        time.sleep(4)
        select_item(lotno)
        lot_rejectlot()
        time.sleep(2)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="6"]') == "驳回"
        Close_current_tab()
        time.sleep(3)

    # 锁定容器
    def test_lockcon_lot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_lotreceive()
        lotno = lot2_add('1234', '1', '1')
        time.sleep(2)
        Close_current_tab()
        time.sleep(2)
        login_lotmg()
        time.sleep(4)
        select_item(lotno)
        lot_lockcontainer(lotno+' 0001')
        time.sleep(2)
        Close_current_tab()
        time.sleep(3)

    # 驳回容器
    def test_rejectcon_lot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_lotreceive()
        lotno = lot2_add('1234', '1', '1')
        time.sleep(2)
        Close_current_tab()
        time.sleep(2)
        login_lotmg()
        time.sleep(4)
        select_item(lotno)
        lot_rejectcontainer(lotno + ' 0001')
        time.sleep(2)
        Close_current_tab()
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-s','test_lotmg.py'])
