# -*- encoding: utf-8 -*-
# @Time : 2021/1/19 11:34 
# @Author : 张丽雯 
# @File : LocationManageData.py 
# @中文描述 :位置管理测试数据
# ---------------------------------------------正常场景-测试数据-------------------------------------------------
code01 = "L001"
code02 = "L002"
code03 = 'L003'
name01 = "name001"
name02 = "name002"
name03 = 'name003'
add_data1 = [(code01,name01)]
# -------------------------------------------------------------------------------------------------------------
# ---------------------------------------------正常场景-编码异常数据----------------------------------------------
code1 = ''  # 不输入
code2 = 'code001'  # 超过最大字符
code3 = 'co@q'  # 含有特殊字符
code4 = '编码'  # 含有汉字
code_abnomal_data1= [(code1,name03)]
code_abnomal_data2 = [(code2,name03)]
code_abnomal_data3 = [(code3,name03),(code4,name03)]
code_abnomal_data4 = [(code02,name03)]  # 已存在
# -------------------------------------------------------------------------------------------------------------
# ---------------------------------------------正常场景-名称异常数据----------------------------------------------
name1 = ''  # 不输入
name2 = 'name123Aname123Anname123Aname123Aname123Aname123Aame123Aname123Aname123Aname123Aname123Aname123Aname1'  # 超过最大字符
name3 = 'name%asd'  # 含有特殊字符
name4 = '-name'  # 以允许的特殊字符开头

name_abnomal_data1= [(code03,name1)]
name_abnomal_data2 = [(code03,name2)]
name_abnomal_data3 = [(code03,name3),(code03,name4)]
name_abnomal_data4 = [(code03,name02)]  # 已存在

edit_name_data1 = [(name1)]
edit_name_data2 = [(name2)]
edit_name_data3 = [(name3),(name4)]
edit_name_data4 = [(name02)]
# -------------------------------------------------------------------------------------------------------------