#coding=utf-8

"""
Created on 2020/10/15
@author: lianxiujuan
@desc: 供应商数据
"""

# --------------------------------------------正常场景测试数据-----------------------------------------------
addcodedata= "aaaa"
add_code1 = 'addcode1'
add_code2 = 'addcode2'
addnamedata = "aaaa"
add_name1 = 'addname1'
add_name2 = 'addname2'
addaddress1data = '地址1'
addaddress2data = '地址2'
addaddress3data = '地址3'
addaddress4data = '地址4'
addleveldata = "级别"
addemaildata = "通讯地址"
addphone1data = "电话号码1"
addphone2data = "电话号码2"
addfaxdata = "传真号码"
editnamedata = "bbbb"
# ---------------------------------------------------------------------------------------------------------

# -------------------------------------------异常场景--编码异常数据-------------------------------------------
code1 = 'code&'  # 编码含有特殊字符
code2 = '-code'  # 以编码规则的特殊字符开头
code3 = ' '  # 编码为空
code4 = 'dfdfdfdfffffffdfdfdfdfffffffdf1'  # 编码超过最大字符30
code5 = addcodedata  # 编码与已有的重复
code_abnormal_list = [(code1,add_name2),(code2,add_name2),(code3,add_name2),(code4,add_name2),(code5,add_name2)]

#,(code3,name),(code4,name),(code5,name)
# -----------------------------------------------------------------------------------------------------------

# -------------------------------------------异常场景--名称异常数据---------------------------------------------
name1 = ' '  # 名称为空
name2 = addcodedata  # 名称与已有的重复
#name3 = '名称最大字符测试100！@#aaas名称最大字符测试100名称最大字符测试100！@#aaas名称最大字符测试100！@#aaas名称最大字符测试100！@#aaas名称最大字符测试100！@#aaas'  # 名称超过最大字符100
name_abnormal_list = [(add_code2,name1),(add_code2,name2)]
edit_name_abnormal = [name1,name2]
# -----------------------------------------------------------------------------------------------------------