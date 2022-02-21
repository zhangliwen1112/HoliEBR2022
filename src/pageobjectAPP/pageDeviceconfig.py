# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagedeviceconfig.py 
# @中文描述 : 设备配置-page


from ElementApp.DeviceconfigPage import *
from src.public.FunctionSet import *


# 进入设备配置界面
def login_deviceconfig():
    new_click(device)
    new_click(deviceconfig)

# 新增设备配置
def deviceconfig_add(addcode, addname):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], addname)
    new_click_ele(ele[2])
    new_click(class1)
    new_click(classyes)
    time.sleep(3)
    new_click(yes_button)
    time.sleep(8)

# 编辑设备配置
def deviceconfig_edit(editname):
    new_click(edit)
    time.sleep(5)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editname)
    new_click(yes_button)
    time.sleep(8)

# 复制设备配置
def deviceconfig_copy(copycode, copyname):
    new_click(copy)
    time.sleep(3)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[0], copycode)
    new_type_double_ele(ele[1], copyname)
    time.sleep(3)
    new_click(yes_button)
    time.sleep(8)

# 失效设备配置
def deviceconfig_noeffect():
    new_click(noeffect)
    new_click(other_yes_button)

# 生效设备配置
def deviceconfig_effect():
    new_click(effect)
    new_click(other_yes_button)
