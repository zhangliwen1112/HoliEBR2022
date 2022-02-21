# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 10:49 
# @Author : 张丽雯 
# @File : weightData.py
# @中文描述 :  砝码配置

# --------------------------------------正常场景-测试数据---------------------------------------
weightname1 = "test_fama1"
weightname2 = "test_fama2"
add_value = "20"
add_unit = 'kg'

edit_value = '70'
edit_unit = 'lb'
# --------------------------------------------------------------------------------------------

# --------------------------------------异常场景-砝码名称-测试数据--------------------------------
name1 = '_weightname'  # 以特殊字符开头
name2 = 'name&weight'  # 名称中含有特殊字符
name3 = 'dfdgdfhfjdf新增砝码砝码dfdgdfhfjdf新增2'  # 超过最大字符30
name4 = ' '  # 为空
name5 = weightname1  # 名称与已有的重复
name_abnormal_list = [(name1, add_value, add_unit),
                      (name2, add_value, add_unit),
                      (name3, add_value, add_unit),
                      (name4, add_value, add_unit),
                      (name5, add_value, add_unit)
                      ]
# --------------------------------------------------------------------------------------------

# --------------------------------------异常场景-砝码重量-测试数据--------------------------------
value1 = 'a'  # 非数字
value2 = '2.3333'  # 小数位数超过3位
value3 = '10000000000'  # 超过最大值9999999999
value4 = ' '  # 为空
add_value_abnormal_list = [(weightname2, value1, add_unit),
                           (weightname2, value2, add_unit),
                           (weightname2, value3, add_unit),
                           (weightname2, value4, add_unit)
                           ]
edit_value_abnormal_list = [(value1, add_unit),
                            (value2, add_unit),
                            (value3, add_unit),
                            (value4, add_unit)
                            ]
# --------------------------------------------------------------------------------------------
