# -*- coding: utf-8 -*- 
# @Time : 2021/1/6 17:46 
# @Author : 张丽雯 
# @File : workpackingData.py 
# @中文描述 : 工单包装
isFinishedContainer = '否'

# -----------------------------------耗用数量-异常场景----------------------------------
num1 = 'a'  # 非数字
num2 = '9999999999' # 超过最大耗用数量
num3 = '1.3333' # 小数位数超过3位

num_list_abnormal = [(num1,isFinishedContainer),
                     (num2,isFinishedContainer),
                     (num3,isFinishedContainer)
                     ]
# ------------------------------------------------------------------------------------

# -----------------------------------退回数量-异常场景----------------------------------
reback_num1 = 'a'  # 非数字
reback_num2 = '9999999999' # 超过最大耗用数量
reback_num3 = '1.3333' # 小数位数超过3位

reback_num_list_abnormal = [(reback_num1),(reback_num2),(reback_num3)]
# ------------------------------------------------------------------------------------