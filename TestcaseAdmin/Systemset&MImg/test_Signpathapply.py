# -*- coding: utf-8 -*- 
# @Time : 2021/1/13 16:23
# @Author : lianxiujuan 
# @File : test_Signpathapply.py 
# @中文描述 : 签名路径应用


import pytest
import sys
from src.pageobjectAdmin.pageSignpathapply import *
from src.public.common.Login import *
from src.public.common.Search_Item import *
from src.pageobjectAdmin.pageMImanage import *
from DataAdmin.MIData import *
from src.pageobjectAdmin.pageSignpath import *
from DataAdmin.SignpathData import *



class Test_Signpathapply:

    def setup_class(self):
        sleep(3)
        # 新增MI
        login_mimanage()
        mimanage_add(signpathmidata)
        new_click(promg)
        # 新增签名路径
        login_signpath()
        time.sleep(2)
        signpath_add(signpathapply_codedata, signpathapply_namedata, signpathapply_leveldata)
        sleep(2)
        search_item("编码", signpathapply_codedata)
        sleep(2)
        signpath_verify()
        new_click(sysset)
        # 进入签名路径界面
        time.sleep(2)
        login_signpathapply()

    def teardown_class(self):
        # 删除MI
        login_mimanage()
        sleep(1)
        search_item("MI编码", signpathmidata)
        sleep(1)
        mimanage_delete()
        sleep(1)
        new_click(promg)
        # 删除签名路径
        login_signpath()
        time.sleep(2)
        search_item("编码", signpathapply_codedata)
        signpath_cancelverify()
        time.sleep(2)
        search_item("编码", signpathapply_codedata)
        signpath_delete()
        sleep(2)
        new_click(sysset)


    # 配置签名路径
    def test_config_signpathapply(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        time.sleep(2)
        signpathapply_config(signpathmidata, signpathapply_codedata)
        search_item("MI编码", signpathmidata)
        time.sleep(2)
        assert new_page_source(signpathmidata)
        assert new_page_source('MI审批')
        assert new_page_source('备注验证')
        assert new_page_source('偏差验证')
        assert new_page_source('MI复核验证')

    # 删除签名路径配置
    def test_delete_signpathapply(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("MI编码", signpathmidata)
        time.sleep(2)
        signpathapply_delete()


        # configitem = ['MI审批', '备注验证', '偏差验证', 'MI复核验证']
        # for i in configitem:
        #     if new_page_source(i):
        #         select_item(i)
        #         sleep(2)
        #         signpathapply_delete()
        #         time.sleep(2)
        #     else:
        #         pass
        # # search_item("MI编码", signpathmidata)
        # time.sleep(2)
        # assert new_page_source(signpathmidata) == False
