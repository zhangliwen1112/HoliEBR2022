# coding=utf-8

"""
Created on 2020/10/15
@author: lianxiujuan
@desc: 标准托盘数据
"""
# ---------------------------------------------正常场景测试数据----------------------------------------------------
palletname = 'pallet1'
addnamedata = "aaaa"
addweightdata = '236.25'
addheightdata = '204'
addlongthdata = '105'
addwidthdata = '23'
addratiodata = "3.87"
addtaredata = "201.32"
editnamedata = "bbbb"
editweightdata = "100.23"
editheightdata = "34"
editlongthdata = "23"
editwidthdata = "45"
editratiodata = "2.67"
edittaredata = "4.26"
# ------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------异常场景测试数据-名称异常--------------------------------------------
name1 = '-name'  # 名称以特殊字符开头
name2 = 'pallet&name'  # 名称含有特殊字符
name3 = ' '  # 名称为空
name4 = '12sgdhsgsdggggggggg12sgdhsgsdggggggggggcontaineqgcontainer001ASAD12sgdhsgsdggggggggggcontainer001ASAD'  # 名称超过最大字符
# 新增&编辑
name_list1 = [(name1, addtaredata), (name2, addtaredata)]
name_list2 = [(name3, addtaredata)]
name_list3 = [(name4, addtaredata)]
# -------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------异常场景测试数据-平均质量异常-----------------------------------------
qty1 = '10000000000'  # 平均质量超过最大值
qty2 = ' '  # 平均质量为空
qty3 = '100.1234'  # 平均质量小数位超过3位
qty4 = '-100'  # 平均质量为负
qty_list1 = [(palletname, addtaredata, qty1)]
qty_list2 = [(palletname, addtaredata, qty2), (palletname, addtaredata, qty3), (palletname, addtaredata, qty4)]
# ------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------异常场景测试数据-高异常----------------------------------------------
high1 = '1000'  # 超过最大值
high2 = ' '  # 为空
high3 = '100.1234'  # 小数位数超过3位
high4 = '-100'  # 为负
high_list1 = [(palletname, addtaredata, addweightdata, high1)]
high_list2 = [(palletname, addtaredata, addweightdata, high2),
              (palletname, addtaredata, addweightdata, high3),
              (palletname, addtaredata, addweightdata, high4)]
# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------异常场景测试数据-长异常----------------------------------------------
long1 = '1000'  # 超过最大值
long2 = ' '  # 为空
long3 = '100.1234'  # 小数位数超过3位
long4 = '-100'  # 为负
long_list1 = [(palletname, addtaredata, addweightdata, addheightdata, long1)]
long_list2 = [(palletname, addtaredata, addweightdata, addheightdata, long2),
              (palletname, addtaredata, addweightdata, addheightdata, long3),
              (palletname, addtaredata, addweightdata, addheightdata, long4)]
# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------异常场景测试数据-宽异常----------------------------------------------
width1 = '1000'  # 超过最大值
width2 = ' '  # 为空
width3 = '100.1234'  # 小数位数超过3位
width4 = '-100'  # 为负
width_list1 = [(palletname, addtaredata, addweightdata, addheightdata, addlongthdata, width1)]
width_list2 = [(palletname, addtaredata, addweightdata, addheightdata, addlongthdata, width2),
               (palletname, addtaredata, addweightdata, addheightdata, addlongthdata, width3),
               (palletname, addtaredata, addweightdata, addheightdata, addlongthdata, width4)]
# --------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------异常场景测试数据-比例异常----------------------------------------------
ratio1 = '10000000000'  # 超过最大值
ratio2 = ' '  # 为空
ratio3 = '10.urllib3介绍'  # 小数位数超过2位
ratio4 = '-1'  # 为负
ratio_list1 = [(palletname, addtaredata, addweightdata, addheightdata, addlongthdata, addweightdata,ratio1)]
ratio_list2 = [(palletname, addtaredata, addweightdata, addheightdata, addlongthdata, addweightdata,ratio2),
               (palletname, addtaredata, addweightdata, addheightdata, addlongthdata, addweightdata,ratio3),
               (palletname, addtaredata, addweightdata, addheightdata, addlongthdata, addweightdata,ratio4)]
# --------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------异常场景测试数据-皮重异常----------------------------------------------
tare1 = '10000000000'  # 超过最大值
tare2 = ' '  # 为空
tare3 = '10.1234'  # 小数位数超过3位
tare4 = '-1'  # 为负
tare_list1 = [(palletname, tare1)]
tare_list2 = [(palletname, tare2)]
tare_list3 = [(palletname, tare3),(palletname, tare4)]
# ---------------------------------------------------------------------------------------------------------------------