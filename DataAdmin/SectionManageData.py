# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 13:43 
# @Author : 张丽雯 
# @File : SectionManageData.py 
# @中文描述 :  区段管理
# -------------------------------------------------正常测试数据--------------------------------------------
section_code01 = "0001"
add_name01 = "section001"
section_code02 = "0002"
add_name02 = "section002"
code03 = "0003"
name03 = "section003"
add_type1 = '生产'
add_type2 = '仓库'

edit_name = "修改区段001"
edit_type = '仓库'
storetype = '原材料'
# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------异常场景测试数据-编码异常------------------------------------------------
code1 = ''  # 为空
code2 = '1'  # 含有1个字符
code3 = '11111'  # 超过最大字符
code4 = '1#23' # 含有特殊字符

add_code_data1 = [(code1,name03)]
add_code_data2 = [(code2,name03),(code3,name03)]
add_code_data3 = [(code4,name03)]
add_code_data4 = [(section_code02,name03)]
# -----------------------------------------------------------------------------------------------------------
# ---------------------------------------异常场景测试数据-名称异常-----------------------------------------------
name1 = ''  # 为空
name2 = 'name123Aname123Anname123Aname123Aname123Aname123Aame123Aname123Aname123Aname123Aname123Aname123Aname1'  # 超过最大字符
name3 = 'name%asd'  # 含有特殊字符
name4 = '-name'  # 以允许的特殊字符开头

add_name_data1 = [(code03,name1)]
add_name_data2 = [(code03,name2)]
add_name_data3 = [(code03,name3),(code03,name4)]
add_name_data4 = [(code03,add_name02)]

edit_name_data1 = [(name1)]
edit_name_data2 = [(name2)]
edit_name_data3 = [(name3),(name4)]
edit_name_data4 = [(add_name02)]
# -----------------------------------------------------------------------------------------------------------