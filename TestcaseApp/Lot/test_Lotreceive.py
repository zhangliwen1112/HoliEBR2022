#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 批次接收
"""

import pytest
import sys
from DataApp.LotReceiveData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageLotreceive import *
from src.public.common.Select_Item import *


class Test_lotreceive:
    def setup_class(self):
        app_login(username, password)
        login_lotreceive()

    # def teardown_class(self):
    #     app_logout()


    # 新增"未处理"批次 后 删除批次
    def test_add_unsolvedlot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        lotno = lot1_add(supplylotdata, lotqtydata)
        time.sleep(3)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="5"]') == "未处理"
        time.sleep(2)
        select_item(lotno)
        lot_delete()
        time.sleep(2)
        assert new_page_source(lotno) == False

    # 新增“已储存”批次 后 取消批次
    def test_add_storedlot(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        lotno = lot2_add(supplylotdata, lotqtydata, con_qtydata)
        time.sleep(3)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="5"]') == "已储存"
        time.sleep(2)
        select_item(lotno)
        lot_cancel()
        time.sleep(2)
        assert new_get_text('//div[@row-index="0"]//div[@aria-colindex="5"]') == "取消"



if __name__ == '__main__':
    pytest.main(['-s','test_lotreceive.py'])

