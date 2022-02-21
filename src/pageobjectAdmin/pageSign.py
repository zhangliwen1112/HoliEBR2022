# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageSign.py
# @中文描述 :  签名设置

from ElementAdmin.SignPage import *
from src.public.FunctionSet import *


# 进入签名设置界面
def login_signset():
    new_click(authmg)
    new_click(signset)

# 新增签名组
def sign_add(addname, addremark):
    new_click(add)
    ele = new_find_elements(name_remark)
    new_send_keys_ele(ele[1], addname)
    new_send_keys_ele(ele[2], addremark)
    new_click(yes_button)

# 编辑签名组
def sign_edit(editname, editremark):
    new_click(edit)
    ele = new_find_elements(name_remark)
    new_type_ele(ele[1], editname)
    new_type_ele(ele[2], editremark)
    new_click(yes_button)

# 删除签名组
def sign_delete():
    new_click(delete)
    new_click(delete_yes_button)
