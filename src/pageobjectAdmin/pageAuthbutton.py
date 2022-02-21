# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageAuthbutton.py
# @中文描述 :  权限按钮

from ElementAdmin.AuthbuttonPage import *
from src.public.common.Search_Item import *


# 进入权限按钮界面
def login_authbutton():
    new_click(authmg)
    new_click(authbu)

# 新增权限按钮
def auth_add(addcode, addname, addinte):
    new_click(add)
    new_send_keys(code, addcode)
    new_send_keys(name, addname)
    new_send_keys(i18n, addinte)
    ele = new_find_elements(submit)
    new_click_ele(ele[2])
    # new_click(yes_button)

# 编辑权限按钮
def auth_edit(editname, editinte):
    new_click(edit)
    new_type_double(name, editname)
    new_send_keys(i18n, editinte)
    ele = new_find_elements(submit)
    new_click_ele(ele[2])
    # new_click(yes_button)

# 删除权限按钮
def auth_delete():
    new_click(delete)
    new_click(delete_yes_button)
