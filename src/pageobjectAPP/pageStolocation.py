# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagestolocation.py
# @中文描述 : 库位-page


from ElementApp.StolocationPage import *
from src.public.FunctionSet import *


# 进入库位界面
def login_stolocation():
    new_click(inventory)
    new_click(storageloction)

# 新增库位-托盘存储/无限容量
def stolocation_add1(addcode, addname):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], addname)
    new_click(infinite)
    new_click(yes_button)

# 新增库位-托盘存储/有限容量
def stolocation_add2(addcode, addname):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], addname)
    new_click(ele[5])
    new_click(kuqu_1)
    new_click(infinite)
    new_click(yes_button)

# 编辑库位
def stolocation_edit(editname):
    new_click(edit)
    time.sleep(2)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editname)
    new_click(yes_button)

# 删除库位
def stolocation_delete():
    new_click(delete)
    new_click(delete_yes_button)
