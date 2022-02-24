# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageSignrule.py
# @中文描述 :  签名规则

from ElementAdmin.SignrulePage import *
from src.public.FunctionSet import *


# 进入签名规则界面
def login_signrule():
    new_click(authmg)
    new_click(signset)

# 新增签名规则
def signrule_add(addname):
    new_click(add)
    ele = new_find_elements(name)
    new_send_keys_ele(ele[3], addname)
    new_click(yes_button)
    # ele = new_find_elements(yes_button)
    # new_click_ele(ele[3])

# 编辑签名规则
def signrule_edit(editname):
    new_click(edit)
    ele = new_find_elements(name)
    new_type_ele(ele[3], editname)
    new_click(yes_button)
    # ele = new_find_elements(yes_button)
    # new_click_ele(ele[3])

# 删除签名规则
def signrule_delete():
    new_click(delete)
    new_click(submit)
    # ele = new_find_elements(yes_button)
    # new_click_ele(ele[2])
