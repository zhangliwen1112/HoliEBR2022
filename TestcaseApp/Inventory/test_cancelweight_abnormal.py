# -*- coding: utf-8 -*- 
# @Time : 2021/5/20 9:43 
# @Author : 张丽雯 
# @File : test_cancelweight_abnormal.py 
# @中文描述 :  取消称量异常场景用例

import pytest
import sys
from src.pageobjectAPP.pageCancelWeight import *
from src.public.common.Close_current_tab import *
from DataApp.CancelWeightData import *


class Test_cancel_weighting_abnormal:
    @pytest.mark.parametrize('label',label_abnormal)
    def test_cancel_execute_abnormal_001(self,label):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_cancel_weight()
        cancel_weight_execute(label)
        assert new_page_source('称量标签不存在')
        Close_current_tab()
