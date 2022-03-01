# -*- coding: utf-8 -*- 
# @Time : 2021/1/14 10:33 
# @Author : 张丽雯 
# @File : pageMaterialSet.py 
# @中文描述 :  物料字段设置界面
from ElementApp.MaterialSetPage import *
from src.public.common.Login import *
from src.public.common.elements import *


# 进入物料字段设置界面

def login_Material_Set():
    new_click(material)
    new_click(materialset)
    sleep(2)
    print('进入物料字段设置页面！')


# 编辑物料字段设置
def Material_Set_edit(isMand=None, isImpac=None):
    new_click(edit)
    sleep(1)
    if isMand == '必填':
        if new_find_element(isselect).get_attribute('aria-checked') == 'false':
            new_click(isMandatory)
            sleep(2)
            if new_page_source('该字段存在内容为“空”的物料数据'):
                new_click(no_button)
                return
    else:
        if new_find_element(isselect).get_attribute('aria-checked') == 'true':
            new_click(isMandatory)

    if isImpac == '影响验证':
        if new_find_elements(isselect)[1].get_attribute('aria-checked') == 'false':
            new_click(isImpactValidation)
    else:
        if new_find_elements(isselect)[1].get_attribute('aria-checked') == 'true':
            new_click(isImpactValidation)

    new_click(yes_button)
    sleep(1)


# 默认值设置: 设置描述、库存单位、效价、有效期、区域、区域信息等
def Material_Set_default(desc_text=None, material_type=None, material_unit=None, material_potency=None, error=None, material_validity=None, va_unit=None,
                         alarm=None, qty=None, rule=None):
    new_click(default)
    sleep(1)
    new_type_double(desc, desc_text)

    # 主要信息
    new_click(type)
    if material_type == '原材料':
        new_click(type1)
    elif material_type == '半成品':
        new_click(type2)
    elif material_type == '包材':
        new_click(type3)
    elif material_type == '成品':
        new_click(type4)
    new_click(unit)
    if material_unit == 'mg':
        new_click(mg)
    elif material_unit == 'g':
        new_click(g)
    elif material_unit == 'lb':
        new_click(lb)
    elif material_unit == 'l':
        new_click(l)
    elif material_unit == 'ml':
        new_click(ml)
    elif material_unit == 'fl':
        new_click(fl)
    elif material_unit == 'un':
        new_click(un)
    elif material_unit == 'kn':
        new_click(kn)
    else:
        new_click(kg)
    sleep(1)
    new_click(potency)
    if material_potency == 'P':
        new_click(P)
    elif material_potency == 'L':
        new_click(L)
    elif material_potency == 'U':
        new_click(U)
    elif material_potency == 'M':
        new_click(M)
    elif material_potency == 'R':
        new_click(R)
    elif material_potency == 'S':
        new_click(S)
    elif material_potency == 'T':
        new_click(T)
    elif material_potency == 'V':
        new_click(V)
    else:
        new_click(N)
    new_click(info_title)
    sleep(1)

    # 称量信息
    inputtext = new_find_elements(input_text)
    new_type_double_ele(inputtext[10], error)
    sleep(1)

    # # 异常处理
    # if is_element_present(error_message):
    #     new_get_text(error_message)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    # elif is_element_present(error_message2):
    #     new_get_text(error_message2)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    # sleep(1)
    new_click(weight_mode)
    new_click(gross)
    new_click(manual)
    new_click(weight_title)
    sleep(1)

    # 批次信息
    new_type_double_ele(inputtext[14], error)
    # # 异常处理
    # if is_element_present(error_message):
    #     new_get_text(error_message)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    # elif is_element_present(error_message2):
    #     new_get_text(error_message2)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    new_click(validity_unit)
    if va_unit == '日':
        new_click(validity_day)
    else:
        new_click(validity_month)
    new_type_double(validity_alarm, alarm)
    # # 异常处理
    # if is_element_present(error_message):
    #     new_get_text(error_message)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    # elif is_element_present(error_message2):
    #     new_get_text(error_message2)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    new_type_double_ele(inputtext[16], qty)
    # # 异常处理
    # if is_element_present(error_message):
    #     new_get_text(error_message)
    #     sleep(1)
    #     new_click(no_button)
    #     return
    # elif is_element_present(error_message2):
    #     new_get_text(error_message2)
    #     sleep(1)
    #     new_click(no_button)
    #     return

    # 区域信息
    new_click(default_pallet)
    new_click(default_pallet1)
    new_click(default_container)
    new_click(default_container1)
    new_click(backup_pallet)
    new_click(backup_pallet1)
    new_click(backup_container)
    new_click(backup_container1)

    # 取样
    new_click(sample_init)
    new_click(sample_init1)
    new_click(sample_zone)
    new_click(sample_zone1)
    new_click(sample_rule)
    if rule == 'A':
        new_click(sample_A)
    elif rule == 'C':
        new_click(sample_C)
    else:
        new_click(sample_Z)
    new_click(yes_button)
    sleep(2)