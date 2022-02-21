# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageAuthbutton.py
# @中文描述 :  OPC设置

from ElementAdmin.OPCsetPage import *
from src.public.FunctionSet import *


# 进入OPC设置界面
def login_opcset():
    new_click(syset)
    new_click(opcset)

# 新增OPC设置
def opcset_add(addcode, addname, addaddress):
    new_click(add)
    ele = new_find_elements(name_code_address)
    new_send_keys_ele(ele[1], addcode)
    new_send_keys_ele(ele[2], addname)
    new_send_keys_ele(ele[3], addaddress)
    new_click(yes_button)

# 编辑OPC设置
def opcset_edit(editaddress):
    new_click(edit)
    ele = new_find_elements(name_code_address)
    new_type_ele(ele[1], editaddress)
    new_click(yes_button)

# 锁定OPC设置
def opcset_lock():
    new_click(lock)
    ele = new_find_elements(other_yes_button)
    new_click_ele(ele[1])

# 解锁OPC设置
def opcset_unlock():
    new_click(unlock)
    ele = new_find_elements(other_yes_button)
    new_click_ele(ele[2])

# 删除OPC设置
def opcset_delete():
    new_click(delete)
    ele = new_find_elements(other_yes_button)
    new_click_ele(ele[0])
