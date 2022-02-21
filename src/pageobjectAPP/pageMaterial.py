# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagematerial.py
# @中文描述 : 物料管理-page


from ElementApp.MaterialPage import *
from src.public.FunctionSet import *


# 进入物料管理界面
def login_material():
    new_click(material)
    time.sleep(1)
    new_click(amaterial)

# 新增物料
def material_add(addcode, addname, adddesc):
    new_click(add)
    time.sleep(6)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], addname)
    new_send_keys(desc, adddesc)
    new_click(yes_button)
    time.sleep(5)

# 编辑物料
def material_edit(editname):
    new_click(edit)
    time.sleep(6)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editname)
    new_click(yes_button)
    time.sleep(5)

# 复制物料
def material_copy(copycode):
    new_click(copy)
    time.sleep(6)
    ele = new_find_elements(allinput)
    new_type_ele(ele[0], copycode)
    new_click(yes_button)
    time.sleep(5)

# 验证物料
def material_verify():
    new_click(verify)
    new_click(other_yes_button)

# 取消验证物料
def material_cancelverify():
    new_click(cancelverify)
    new_click(other_yes_button)

# 失效物料
def material_noeffect():
    new_click(noeffect)
    new_click(other_yes_button)

# 生效物料
def material_effect():
    new_click(effect)
    new_click(other_yes_button)
