# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 10:56 
# @Author : 张丽雯 
# @File : cleanData.py 
# @中文描述 :  清洁配置

add_code1="code1q"
add_code2 = 'code2c'
name="clean002"
ruletype="工单"
text = name

# ------------------------------------清洁配置-新增-编码规则-异常数据----------------------------------
code1 = '_code'  # 以特殊字符开头
code2 = 'code&rule'  # 含有规定外的特殊字符
code3 = '1111111111111111111111111111112code'  # 超过最大字符30
code4 = ' '  # 为空
code5 = add_code1  # 与已有的重复
code_abnormal_data = [(code1,name),(code2,name),(code3,name),(code4,name),(code5,name)]
# -------------------------------------------------------------------------------------------------
# ------------------------------------清洁配置-新增-编码规则-异常数据----------------------------------
name1 = '_name'  # 以特殊字符开头
name2 = 'name&3'  # 含有规定外的特殊字符
name3 = 'guize123456dhfdhf规则名称namenamenamenamena3e123456dhfdhf规则名称namenamenamenamenameguize123456dhfdhf规则名称nam'  # 超过最大字符100
name4 = ' '  # 为空
name_abnormal_data = [(add_code2,name1),(add_code2,name2),(add_code2,name3),(add_code2,name4)]
edit_name_abnormal_list = [(name1),(name2),(name3),(name4)]
# -------------------------------------------------------------------------------------------------