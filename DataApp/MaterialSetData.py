# -*- coding: utf-8 -*- 
# @Time : 2021/1/14 10:52 
# @Author : 张丽雯 
# @File : MaterialSetData.py 
# @中文描述 :  物料字段设置用例数据
# ---------------------------------------------正常场景数据------------------------------------------------------------
search_value = '取样'

edit_text1 = '必填'
edit_text2 = '影响验证'

# 物料默认字段设置
desc_text = 'testdescmaterials'
material_type = '原材料'
material_unit = 'kg'
material_potency = 'N'
material_validity = '5'
va_unit = '日'
alarm = '1'
qty = '15'
rule = 'A'
error = '2'
# -------------------------------------------------------------------------------------------------------------------
# -----------------------------------------异常数据--称量间误差异常------------------------------------------------------
weight_error1 = "1.23"  # 非整数，小数
weight_error2 = "10000" # 超过边界值9999
weight_error_abnormal_list = [(desc_text, material_type, material_unit, material_potency, weight_error1,
                               material_validity, va_unit, alarm, qty, rule),
                              (desc_text, material_type, material_unit, material_potency, weight_error2,
                               material_validity, va_unit, alarm, qty, rule)
                              ]
# -----------------------------------------异常数据--有效期异常----------------------------------------------------------
material_validity1 = "1.55"  # 非整数
material_validity2 = "100000"  # 大于99999
material_validity_abnormal_list = [
    (desc_text, material_type, material_unit, material_potency, error, material_validity1, va_unit, alarm, qty, rule),
    (desc_text, material_type, material_unit, material_potency, error, material_validity2, va_unit, alarm, qty, rule)
]
# -----------------------------------------异常数据--有效期预警异常------------------------------------------------------
alarm1 = "12.1"  # 非整数
alarm2 = "100000"  # 大于99999
alarm_abnormal_list = [
    (desc_text, material_type, material_unit, material_potency, error, material_validity, va_unit, alarm1, qty, rule),
    (desc_text, material_type, material_unit, material_potency, error, material_validity, va_unit, alarm2, qty, rule)
]

# -----------------------------------------异常数据--取样量异常---------------------------------------------------------
qty1 = "12.1234"  # 小数位数不满足，如4位小数
qty2 = "10000000000"  # 大于9999999999
qty_abnormal_list = [
    (desc_text, material_type, material_unit, material_potency, error, material_validity, va_unit, alarm, qty1, rule),
    (desc_text, material_type, material_unit, material_potency, error, material_validity, va_unit, alarm, qty2, rule)
]
# -------------------------------------------------------------------------------------------------------------------
