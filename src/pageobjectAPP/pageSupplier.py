# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagesupplier.py
# @中文描述 : 供应商-page


from ElementApp.SupplierPage import *
from src.public.FunctionSet import *
from src.public.common.elements import *

# 进入供应商界面


def login_supplier():
    new_click(inventory)
    new_click(supplier)

# 新增供应商
def supplier_add(addcode, addname, addaddress1='', addaddress2='', addaddress3='',
                 addaddress4='', addlevel='', addemail='', addphone1='', addphone2='', addfax=''):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    sleep(1)
    new_send_keys_ele(ele[1], addname)
    new_send_keys_ele(ele[2], addaddress1)
    new_send_keys_ele(ele[3], addaddress2)
    new_send_keys_ele(ele[4], addaddress3)
    new_send_keys_ele(ele[5], addaddress4)
    new_send_keys_ele(ele[6], addlevel)
    new_send_keys(email, addemail)
    new_send_keys_ele(ele[7], addphone1)
    new_send_keys_ele(ele[8], addphone2)
    new_send_keys_ele(ele[9], addfax)
    new_click(yes_button)
    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancle)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancle)
# 编辑供应商
def supplier_edit(editname):
    new_click(edit)
    time.sleep(2)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editname)
    new_click(yes_button)
    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancle)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancle)

# 删除供应商
def supplier_delete():
    new_click(delete)
    sleep(0.5)
    new_click(delete_yes_button)
