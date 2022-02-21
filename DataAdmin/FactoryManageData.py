# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 17:54 
# @Author : 张丽雯 
# @File : FactoryManageData.py 
# @中文描述 :  厂区管理
# ---------------------------------------------正常场景测试数据-------------------------------------------
code01 = '11'
name01 = 'factory001'
code02 = '12'
name02 = 'factory002'
code03 = '13'
name03 = 'factory003'
Adr1 = "东北角"
Adr2 = "西北角"
Adr3 = "第三厂区"
Adr4 = "东南角"

edit_name = '修改厂区001'
# -------------------------------------------------------------------------------------------------------
# ---------------------------------------异常场景测试数据-编码异常---------------------------------------
code1 = ''  # 为空
code2 = '1'  # 含有1个字符
code3 = '111'  # 超过最大字符
code4 = '1#'  # 含有特殊字符
code5 = ' '  # 输入空格

add_code_data1 = [(code1, name03)]
add_code_data2 = [(code2, name03), (code3, name03)]
add_code_data3 = [(code4, name03)]
add_code_data4 = [(code02, name03)]
add_code_data5 = [(code5, name03)]
# -------------------------------------------------------------------------------------------------------
# ---------------------------------------异常场景测试数据-名称异常---------------------------------------
name1 = ''  # 为空
name2 = 'name123Aname123Anname123Aname123Aname123Aname123Aame123Aname123Aname123Aname123Aname123Aname123Aname1'  # 超过最大字符
name3 = 'name%asd'  # 含有特殊字符
name4 = '-name'  # 以允许的特殊字符开头

add_name_data1 = [(code03, name1)]
add_name_data2 = [(code03, name2)]
add_name_data3 = [(code03, name3), (code03, name4)]
add_name_data4 = [(code03, name02)]

edit_name_data1 = [(name1)]
edit_name_data2 = [(name2)]
edit_name_data3 = [(name3), (name4)]
edit_name_data4 = [(name02)]
# ------------------------------------------------------------------------------------------------------
