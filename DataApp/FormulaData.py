# -*-coding:GBK -*-
# --------------------------------------------正常场景-----------------------------------------------------
# 新增物料数据
add_name1 = "formulaname001"
add_type1 = "测试/研发"
add_num = '1000'
r_unit = 'mg'
add_weight = "200"
w_unit = 'g'
add_name2 = "formulaname002"
add_type2 = "生产/临床"

# 编辑数据
edit_name = '修改处方'
edit_num = '2000.urllib3介绍'
edit_weight = '500.55'
edit_r_unit = 'kg'
edit_w_unit = 'kg'

# 新增处方物料单位
m_unit = 'kg'
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------异常场景---处方名称异常----------------------------------------------
name1 = "@urllib3介绍"  # 以特殊字符开头
name2 = "F&a"   # 包含特殊字符
name3 = "ASDchufang123_dfd45/dfdf处方ASDchufang123_dfd45/dfdf处方ASDchufang123_dfd45/dfdf处方dfd45/dfdf处方123fgfgf101"  # 超过100字符，101字符
name4 = " "     # 空字符
abnormal_name = [(name1, add_num, r_unit, add_weight, w_unit),
                 (name2, add_num, r_unit, add_weight, w_unit),
                 (name3, add_num, r_unit, add_weight, w_unit),
                 (name4, add_num, r_unit, add_weight, w_unit)
                 ]
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------异常场景---参考数量异常----------------------------------------------
num1 = "1.1234"  # 小数位数超过3位
num2 = "a"  # 非数字
num3 = "10000000000"  # 超过最大值
abnormal_num = [(add_name1, num1, r_unit, add_weight, w_unit),
                (add_name1, num2, r_unit, add_weight, w_unit),
                (add_name1, num3, r_unit, add_weight, w_unit)
                ]
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------异常场景---等价称量异常----------------------------------------------
weight1 = "1.1234"  # 小数位数超过3位
weight2 = "a"  # 非数字
weight3 = "10000000000"  # 超过最大值
abnormal_weight = [(add_name1, add_num, r_unit, weight1, w_unit),
                   (add_name1, add_num, r_unit, weight2, w_unit),
                   (add_name1, add_num, r_unit, weight3, w_unit)
                   ]
# -----------------------------------------------------------------------------------------------------------
