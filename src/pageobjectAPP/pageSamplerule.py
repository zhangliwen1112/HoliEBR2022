# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagesamplerule.py
# @中文描述 : 取样规则-page


from ElementApp.SamplerulePage import *
from src.public.FunctionSet import *


# 进入取样规则界面
def login_samplerule():
    new_click(material)
    new_click(samplerule)

# 新增取样规则
def samplerule_add(addcode, adddesc, addend, addcontainer1, addcontainer2):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys(desc, adddesc)
    new_send_keys_ele(ele[2], addend)
    new_send_keys_ele(ele[3], addcontainer1)
    new_click(addscope)
    new_send_keys_ele(ele[3], addcontainer2)
    new_click(addscope)
    new_click(yes_button)

# 新增取样规则
def samplerule_add_abnormal(addcode, adddesc, addend, addcontainer):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys(desc, adddesc)
    new_send_keys_ele(ele[2], addend)
    new_send_keys_ele(ele[3], addcontainer)
    new_click(addscope)

# 编辑取样规则
def samplerule_edit(editdescdata):
    new_click(edit)
    time.sleep(2)
    new_type_double(desc, editdescdata)
    new_click(yes_button)

# 删除取样规则
def samplerule_delete():
    new_click(delete)
    new_click(delete_yes_button)
