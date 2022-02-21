# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageLotreceive.py
# @中文描述 : 批次接收-page


from ElementApp.LotreceivePage import *
from src.public.FunctionSet import *
from src.public.common.elements import *


# 进入批次接收界面
def login_lotreceive():
    new_click(lotmg)
    new_click(lotreceive)

# 新增"未处理"批次
def lot1_add(addsupplylot, addlotqty):
    new_click(add)
    time.sleep(2)
    ele = new_find_elements(supply_material)
    new_click_ele(ele[2])
    new_click(supplysele)
    new_click(supply_yes)
    new_click_ele(ele[3])
    new_click(materialsele)
    new_click(material_yes)
    new_send_keys(supplylot, addsupplylot)
    new_send_keys(lot_qty, addlotqty)
    ele = new_find_elements(yes)
    new_click_ele(ele[0])
    new_click(primary_button)
    time.sleep(2)
    return new_get_text('//div[@row-index="0"]//div[@aria-colindex="8"]')


# 新增"已储存"批次
def lot2_add(addsupplylot, addlotqty, addconqty):
    new_click(add)
    time.sleep(2)
    ele = new_find_elements(supply_material)
    new_click_ele(ele[2])
    new_click(supplysele)
    new_click(supply_yes)
    new_click_ele(ele[3])
    new_click(materialsele)
    new_click(material_yes)
    time.sleep(1)
    new_send_keys(supplylot, addsupplylot)
    new_send_keys(lot_qty, addlotqty)
    new_click(pack)
    time.sleep(2)
    new_send_keys(container_qty, addconqty)
    ele = new_find_elements(yes)
    new_click_ele(ele[0])
    time.sleep(2)
    new_click(approve)
    time.sleep(4)
    new_click(label)
    time.sleep(2)
    new_click(label_yes)
    time.sleep(2)
    new_click(sample)
    time.sleep(2)
    new_click(store)
    time.sleep(2)
    new_click(close)
    time.sleep(2)
    return new_get_text('//div[@row-index="0"]//div[@aria-colindex="8"]')

# 删除批次
def lot_delete():
    new_click(delete)
    new_click(red_button)

# 取消批次
def lot_cancel():
    new_click(cancel)
    new_click(red_button)
