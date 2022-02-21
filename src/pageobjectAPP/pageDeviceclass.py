# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagedeviceclass.py 
# @中文描述 : 设备类别-page


from ElementApp.DeviceclassPage import *
from src.public.FunctionSet import *


# 进入设备类别界面
def login_deviceclass():
    new_click(device)
    new_click(deviceclass)

# 新增设备类别
def deviceclass_add(addcode, addname):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], addname)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[0])

# 编辑设备类别
def deviceclass_edit(editname):
    new_click(edit)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editname)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[0])

# 复制设备类别
def deviceclass_copy(copycode, copyname):
    new_click(copy)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[0], copycode)
    new_type_double_ele(ele[1], copyname)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[0])

# 失效设备类别
def deviceclass_noeffect():
    new_click(noeffect)
    time.sleep(2)
    new_click(other_yes_button)

# 生效设备类别
def deviceclass_effect():
    new_click(effect)
    time.sleep(2)
    new_click(other_yes_button)
