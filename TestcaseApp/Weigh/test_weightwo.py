# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 9:25 
# @Author : 张丽雯 
# @File : test_weightwo.py 
# @中文描述 :  称量工单-用例
import sys
import pytest
from DataApp.WeightWoData import *
from src.pageobjectAPP.pageWeightwo import *
from src.public.common.Close_current_tab import Close_current_tab
from src.public.common.Search_Item import *


class Test_Weightwo:
    def setup_class(self):
        app_login(username, password)
        login_weightwo()

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 称量工单-筛选工单
    def test_weightwo_search(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码', WO1)
        sleep(1)
        assert is_text_present(WO1)

    # 称量工单-净重模式-结束称量
    @pytest.mark.parametrize('n,tare,selectmode', over_net)
    def test_weightwo_net_001(self, n, tare, selectmode):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_net(n, tare, selectmode)
        sleep(1)
        assert new_page_source('保存成功')

    # 称量工单-净重模式-取消称量
    @pytest.mark.parametrize('n,tare,selectmode', cancel_net)
    def test_weightwo_net_002(self, n, tare, selectmode):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_net(n, tare, selectmode)
        sleep(1)
        assert new_js_text(input_container) == ''

    # 称量工单-净重模式-相同容器
    @pytest.mark.parametrize('n,tare,selectmode', same_net)
    def test_weightwo_net_003(self, n, tare, selectmode):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_net(n, tare, selectmode)
        sleep(1)
        assert new_page_source('保存成功')

    # 称量工单-人工输入模式
    @pytest.mark.parametrize('n, netvalue, tarevalue', manual_list)
    def test_weightwo_manual(self, n, netvalue, tarevalue):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_manual(n, netvalue, tarevalue)
        assert new_page_source('保存成功')

    # 称量工单-计数称量模式
    @pytest.mark.parametrize('n,tare',count_list)
    def test_weightwo_count(self,n,tare):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码', WO2)
        sleep(1)
        weight_wo_count(n,tare)
        sleep(1)
        assert new_page_source('保存成功')

    # 称量工单-批次信息
    def test_weightwo_lot_detail(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_lot_detail('0')
        sleep(1)
        assert new_js_text(input_container) != ''

    # 称量工单-取消称量
    @pytest.mark.parametrize('n,cancel1,cancel2', [('0', '取消称量', '否'), ('0', '否', '取消称量')])
    def test_weightwo_cancel_weight(self, n, cancel1, cancel2):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_cancel(n, cancel1, cancel2)
        sleep(2)
        assert new_js_text(input_container) == ''

	 # 毛重称量
    def test_gross_weigh(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        grossweighmode("0.2")
        time.sleep(2)

    # RM混合
    def test_rmmix_weigh(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        rmweighmode("0.2")
        time.sleep(2)

    # 称量次数
    def test_weigh_times(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sleep(7)
        times1 = new_js_text(weightimes)
        grossweighmode("0.2")
        time.sleep(2)
        times2 = new_js_text(weightimes)
        assert int(times1)+1 == int(times2)

    # 总重量
    def test_total_weigh(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        sleep(7)
        weigh1 = new_js_text(totalweigh)
        grossweighmode("0.2")
        time.sleep(2)
        weigh2 = new_js_text(totalweigh)
        assert float(weigh1)+3.087 == float(weigh2)

    # 强制称量
    def test_force_weigh(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        forceweigh()
        assert new_page_source('称量完成')

    # 物料信息
    def test_material_info(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        material_info()
        sleep(1)
        assert new_get_text(stage) == '0001'
        assert new_get_text(seq) == '0001'
        assert new_get_text(dose) == '1'
        new_click(closed)

    # 托盘标签
    def test_pallet_label(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        pallet_label()
        assert new_get_text(alert_txt) == '打印信息发送成功'


    # 输入容器识别号-容器号不存在
    @pytest.mark.parametrize('CID', ['1232323'])
    def test_weightwo_containerid_adnormal_001(self, CID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_container_ID(CID)
        sleep(1)
        assert is_text_present('不存在该批次信息的容器')

    # 输入容器识别号-容器已过期
    @pytest.mark.parametrize('CID', ['RL00000033 0001'])
    def test_weightwo_containerid_adnormal_002(self, CID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        weight_wo_container_ID(CID)
        sleep(1)
        assert is_text_present('容器已过期')

    # 净重称量模式-剩余量正确性比对
    def test_weightwo_net_remain(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        # 选择称量工单物料
        new_click(material(n3))
        sleep(1)
        remain1 = float(new_js_text(remain_number))
        weight_wo_net(n3, tarevalue1, selectmode1)
        sleep(1)
        remain2 = float(new_js_text(remain_number))
        net = round(remain1 - remain2, 3)
        weight_wo_net(n3, tarevalue1, selectmode1)
        sleep(1)
        remain3 = round(float(new_js_text(remain_number)), 3)
        assert remain3 == round(remain2 - net, 3)

    # 人工输入模式-剩余量正确性比对
    def test_weightwo_manual_remain(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        # 选择称量工单物料
        new_click(material(n3))
        sleep(1)
        remain1 = float(new_js_text(remain_number))
        weight_wo_manual(n3, '10', '0.002')
        sleep(1)
        remain2 = float(new_js_text(remain_number))
        assert remain2 == remain1 - 10
    # 净重称量模式-净重正确性比对
    def test_weightwo_net_netvalue(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        # 选择称量工单物料
        weight_wo_net_netvalue(n3, tarevalue1)
        sleep(1)
        netvalue = new_js_text(net_number)
        #  3.090是秤的度数，这值根据实际情况而定
        assert netvalue == '3.090'
        new_click(CanWeigh)

    # 净重称量模式-皮重正确性比对
    def test_weightwo_net_tarevalue(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        # 选择称量工单物料
        weight_wo_net_netvalue(n3, '0.033')
        sleep(1)
        tare_value = new_js_text(tare_number)
        assert tare_value == '0.033'
