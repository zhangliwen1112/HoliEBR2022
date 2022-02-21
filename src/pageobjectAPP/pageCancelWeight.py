# -*- coding: utf-8 -*- 
# @Time : 2021/2/1 11:28 
# @Author : 张丽雯 
# @File : pageCancelWeight.py
# @中文描述 :  取消称量--退料、取消称量
import sys

from ElementApp.CancelWeightPage import *
from src.public.common.Login import *

# ---------------------------------------------退料界面-------------------------------------------------
from src.public.common.elements import error_message


def login_returned_materials():
    new_click(inventory)
    new_click(cancelweight)
    new_click(returned_mater)
    sleep(2)
    print('进入退料页面!')

def returned_materials_execute(isdeletewo,label,isstore):
    if isdeletewo == '是':
        if new_find_element(isselect).get_attribute('aria-checked') == 'true':
            new_type(weight_label,label)
        else:
            new_click(delete_wo)
            new_type(weight_label, label)
    else:
        if new_find_element(isselect).get_attribute('aria-checked') == 'true':
            new_click(delete_wo)
            new_type(weight_label,label)
        else:
            new_type(weight_label, label)
    if isstore == '新容器':
        new_click(new_container)
        new_click(factory)
        new_click(select1)
        sleep(1)
        new_click(select_submit)
        sleep(1)
        new_click(area)
        new_click(area1)
        new_click(section)
        new_click(section1)
        new_click(reservoir)
        new_click(reservoir1)
        new_click(stolocation)
        new_click(stolocation1)
    else:
        new_click(exist_container)
        sleep(1)
        new_click(first_container)
    new_click(execute)
    sleep(2)
    if new_page_source('目标库位的库区与物料上设定的默认/备用库区不兼容,是否继续执行该操作？'):
        new_click(yes_button)
    sleep(2)
# ------------------------------------------------------------------------------------------------------

# --------------------------------------------取消称量----------------------------------------------------
def login_cancel_weight():
    new_click(inventory)
    new_click(cancelweight)
    new_click(cancel_weight)
    sleep(2)
    print('进入取消称量页面!')

def cancel_weight_execute(label):
    new_click(c_factory)
    new_click(select1)
    new_click(select_submit)
    new_click(c_area)
    new_click(area1)
    new_click(c_section)
    new_click(section1)
    new_click(c_reservoir)
    new_click(reservoir1)
    new_click(c_stolocation)
    new_click(stolocation1)
    for i in label:
        new_type_double(weight_label,i)
        sleep(1)
        new_click(any_ele)
        sleep(2)
        if is_element_present(error_message):
            return
        else:
            new_click(add)
            sleep(1)
            if new_page_source('执行后会将该次称量加入待取消列表，是否继续？'):
                new_click(yes_button)
    new_click(execute)
    sleep(1)
    if new_page_source('目标库位的库区与物料上设定的默认/备用库区不兼容,是否继续执行该操作？'):
        new_click(yes_button)
    sleep(1)
    if new_page_source('执行后会为取消称量的物料创建一个新容器，是否继续？'):
        new_click(yes_button)
    sleep(1)


