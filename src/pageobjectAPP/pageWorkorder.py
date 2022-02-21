# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageworkordermg.py
# @中文描述 : 工单管理-page


from ElementApp.WorkorderPage import *
from src.public.FunctionSet import *
from src.public.common.elements import *


# 进入工单管理界面
def login_wo():
    new_click(workorder)
    new_click(aworkorder)


# 新增工单
def wo_add(addwoqty='100.23', wotype='生产工单'):
    new_click(add)
    time.sleep(2)
    ele = new_find_elements(formula)
    new_click_ele(ele[1])
    new_click(formulasele)
    new_click(formulayes)
    sleep(1)
    new_type_double(qty, addwoqty)
    new_click(type)
    if wotype == '称量工单':
        new_click(type_weight)
    elif wotype == '包装工单':
        new_click(type_pack)
    elif wotype == '其他工单':
        new_click(type_other)
    else:
        new_click(type_produce)
    new_click(yes_button)
    time.sleep(2)
    return new_get_text(firstdata_app)


# 编辑工单
def wo_edit(editqty):
    new_click(edit)
    new_type_double(qty, editqty)
    new_click(yes_button)


# 复制工单
def wo_copy():
    new_click(copy)
    new_click(yes_button)


# 修订工单
def wo_mod(modqty):
    new_click(modify)
    new_click(womaterial)
    new_click(firstmaterial)
    new_type_double(allqty, modqty)
    new_click(weight)
    new_click(room)
    new_click(packing)
    new_click(save)
    new_click(yes_button)
    sleep(2)
    if new_page_source('超过主工单的数量'):
        new_click(other_yes_button)


# 发布工单
def wo_release():
    new_click(release)
    time.sleep(2)
    ele = new_find_elements(re_input)
    new_click_ele(ele[6])
    time.sleep(1)
    new_click(workcentersele)
    time.sleep(2)
    ele = new_find_elements(workcenteryes)
    new_click_ele(ele[4])
    time.sleep(1)
    ele = new_find_elements(re_input)
    new_click_ele(ele[7])
    time.sleep(2)
    new_click(misele)
    time.sleep(1)
    new_click(miyes)
    time.sleep(1)
    new_click(re_yes_button)
    time.sleep(1)


# 取消发布工单
def wo_cancelre():
    new_click(cancelre)


# 取消工单
def wo_cancel():
    new_click(cancel)
    new_click(other_yes_button)


# 终止工单
def wo_stop():
    new_click(stop)
    new_click(other_yes_button)


# 关闭工单
def wo_close():
    new_click(close)
    new_click(other_yes_button)
