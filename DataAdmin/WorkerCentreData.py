# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 13:53 
# @Author : 张丽雯 
# @File : WorkerCentreData.py 
# @中文描述 :  工作中心-工作中心页面
# ------------------------------------------------正常测试数据--------------------------------------------------
add_code1 = '001'
add_code2 = '002'
add_code3 = '003'
add_name1 = '新增工作中心001'
add_name2 = "workercenter002"
add_name3 = "workercenter003"
edit_name = '修改工作中心001'
# -------------------------------------------------------------------------------------------------------------

# -----------------------------------------------异常测试数据-编码异常---------------------------------------------
code1 = ''  # 为空
code2 = 'workercode11111111201'  # 超过最大值
code3 = 'code&1'  # 含有特殊字符
code4 = 'code编码'  # 含有汉字
code5 = 'code 2'  # 含有空格
code_abnormal_data1 = [(code1,add_name3)]
code_abnormal_data2 = [(code2,add_name3)]
code_abnormal_data3 = [(code3,add_name3),(code4,add_name3),(code5,add_name3)]
code_abnormal_data4 = [(add_code1,add_name3)]  # 已重复
# --------------------------------------------------------------------------------------------------------------

# -----------------------------------------------异常测试数据-名称异常---------------------------------------------
name1 = ''  # 为空
name2 = 'name名称123ASDname名namname名称123ASDname名称123ASDname名称123ASDname名称123ASDe名称123ASDname名称123ASD称123ASDname名'  # 超过最大字符
name3 = 'name$q'  # 含有特殊字符
name4 = '/name'  # 已允许的特殊字符开头
name_abnormal_data1 = [(add_code3,name1)]
name_abnormal_data2 = [(add_code3,name2)]
name_abnormal_data3 = [(add_code3,name3),(add_code3,name4)]
name_abnormal_data4 = [(add_code3,add_name2)]
# --------------------------------------------------------------------------------------------------------------
