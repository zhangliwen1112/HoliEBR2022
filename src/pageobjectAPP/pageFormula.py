# coding:utf-8
# @Time : 2021/10/16 14:50
# @Author : 张丽雯
# @File : pageformula.py
# @中文描述 :  处方管理
from ElementApp.FormulaPage import *
from src.public.common.Login import *
from src.public.common.elements import *


# 进入处方页面
def login_formula():
    new_click(formula)
    print('进入处方管理页面')


# 点击复制
def formula_copy():
    new_click(copy)


# 新增处方页面
def formula_add_web(formula_name, formula_type, reference_num, reference_unit, equivalent_weight, weight_unit):
    new_click(add)
    sleep(1)
    new_type(name, formula_name)
    sleep(1)
    new_click(type)
    if formula_type == '测试/研发':
        new_click(type1)
    else:
        new_click(type2)
    new_click(product_code)
    sleep(1)
    new_click(product_search1)
    new_type(r_num, reference_num)
    sleep(1)
    new_click(r_unit)
    if reference_unit == 'mg':
        new_click(unit1)
    elif reference_unit == 'g':
        new_click(unit2)
    else:
        new_click(unit3)
    new_type(weight, equivalent_weight)
    sleep(1)
    new_click(w_unit)
    if weight_unit == 'mg':
        driver.find_elements_by_xpath(unit1)[1].click()
    elif weight_unit == 'g':
        driver.find_elements_by_xpath(unit2)[1].click()
    elif weight_unit == 'lb':
        driver.find_elements_by_xpath(unit4)[1].click()
    else:
        driver.find_elements_by_xpath(unit3)[1].click()
    sleep(1)
    new_click(add_submit)
    sleep(1)
    if new_page_source('请按照格式要求填写数据'):
        new_click(add_cancle)
    sleep(1)


# 编辑 处方页面
def formula_edit_web(formula_name, reference_num, reference_unit, equivalent_weight, weight_unit):
    new_click(edit)
    sleep(1)
    new_type_double(name, formula_name)
    new_click(type)
    new_click(type1)
    new_click(product_code)
    sleep(1)
    new_click(product_search2)
    new_type_double(r_num, reference_num)
    sleep(1)
    new_click(r_unit)
    if reference_unit == 'mg':
        new_click(unit1)
    elif reference_unit == 'g':
        new_click(unit2)
    else:
        new_click(unit3)
    new_type_double(weight, equivalent_weight)
    sleep(1)
    new_click(w_unit)
    if weight_unit == 'mg':
        driver.find_elements_by_xpath(unit1)[1].click()
    elif weight_unit == 'g':
        driver.find_elements_by_xpath(unit2)[1].click()
    elif weight_unit == 'lb':
        driver.find_elements_by_xpath(unit4)[1].click()
    else:
        driver.find_elements_by_xpath(unit3)[1].click()
    new_click(add_submit)
    sleep(1)
    if new_page_source('请按照格式要求填写数据'):
        new_click(add_cancle)
    sleep(1)


# 新增处方物料
def formula_add_material_001(maternum, unit):
    new_click(material_add)
    sleep(1)
    new_click(material_name)
    driver.find_elements_by_xpath(material_search1)[1].click()
    new_click(material_tail)
    # 获取补偿器输入框是否可点击
    value = new_get_text(compensator)
    if len(value) == 0:
        new_click(compensator)
        new_click(no_compensator)
        new_type(material_num, maternum)
        sleep(1)
        new_click(material_unit)
        if unit == 'mg':
            driver.find_elements_by_xpath(unit1)[2].click()
        elif unit == 'g':
            driver.find_elements_by_xpath(unit2)[2].click()
        elif unit == 'lb':
            driver.find_elements_by_xpath(unit4)[2].click()
        else:
            driver.find_elements_by_xpath(unit3)[2].click()
        new_click(material_yes)
    else:
        new_type(material_num, maternum)
        sleep(1)
        new_click(material_unit)
        if unit == 'mg':
            driver.find_elements_by_xpath(unit1)[2].click()
        elif unit == 'g':
            driver.find_elements_by_xpath(unit2)[2].click()
        elif unit == 'lb':
            driver.find_elements_by_xpath(unit4)[2].click()
        else:
            driver.find_elements_by_xpath(unit3)[2].click()
        new_click(material_yes)
    sleep(1)


# 删除处方物料1
def formula_delete_material():
    new_click(material_delete)
    sleep(1)
    new_click(yes_button)


# 提交处方
def formula_submit():
    new_click(submit)
    sleep(1)
    new_click(yes_button)


# 批准处方
def formula_approve():
    new_click(approve)
    sleep(1)
    new_click(yes_button)

# 验证处方
def formula_verify():
    new_click(verify)
    sleep(1)
    new_click(yes_button)

# 复制处方
def formula_copy_formula():
    new_click(copy)
    sleep(1)
    new_click(add_submit)


# 修订处方
def formula_revise():
    new_click(revise)
    sleep(1)
    new_click(add_submit)


# 失效处方
def formula_noeffect():
    new_click(noeffect)
    sleep(1)
    new_click(yes_button)


# 查看处方
def formula_check():
    new_click(check)
    sleep(1)
    new_click(add_submit)
