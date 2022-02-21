# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:43 
# @Author : 张丽雯 
# @File : DeviceData.py 
# @中文描述 :  外部设备
# --------------------------------------------------正常场景测试数据--------------------------------------------------
device_code01 = 'dcode01'
device_name01 = 'weighting01'
device_type01 = '手环'
device_status01 = '在线'
device_address01 = 'ws://172.26.15.5:3000/api/ws/scale'
device_des01 = '电子秤新增'

device_code02 = 'dcode02'
device_name02 = 'weighting02'
device_type02 = '电子秤'
device_status02 = '注册'
device_address02 = 'ws://172.26.15.5:3000/api/ws/rfid'
device_des02 = '手环新增'

device_code03 = 'dcode03'
device_name03 = '打印机新增03'
device_type03 = '打印机'
device_status03 = '离线'
device_address03 = 'http://172.26.15.5:3000/api/print'
device_des03 = '打印机新增'

device_code04 = 'dcode04'
device_name04 = '新增04'
device_type04 = '打印机'
device_status04 = '注销'
device_address04 = 'http://172.26.15.5:3000/api/print'
device_des04 = '打印机注销'

add_data = [
    (device_code01, device_name01, device_type01, device_status01, device_address01, device_des01),
    (device_code02, device_name02, device_type02, device_status02, device_address02, device_des02),
    (device_code03, device_name03, device_type03, device_status03, device_address03, device_des03),
    (device_code04, device_name04, device_type04, device_status04, device_address04, device_des04)
]

edit_name01 = '电子秤修改'
edit_type01 = '电子秤'
edit_status01 = '注销'
edit_address01 = 'ws://172.26.15.5:3000/api/ws/scale'
edit_des01 = '电子秤状态修改'

delete_data = [device_code01, device_code02, device_code03,device_code04]
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------异常场景测试数据-编码-------------------------------------------------
code1 = ''  # 为空
code2 = 'devicecode11111111201'  # 超过最大值
code3 = 'devic&1'  # 含有特殊字符
code4 = 'devic编码'  # 含有字母数字
code5 = 'devic 2'  # 含有空格
code_abnormal_data1 = [(code1, device_name03, device_type01, device_status01, device_address03, device_des03)]
code_abnormal_data2 = [(code2, device_name03, device_type01, device_status02, device_address03, device_des03)]
code_abnormal_data3 = [
    (code3, device_name03, device_type01, device_status03, device_address03, device_des03),
    (code4, device_name03, device_type01, device_status03, device_address03, device_des03),
    (code5, device_name03, device_type01, device_status03, device_address03, device_des03)
]
code_abnormal_data4 = [(device_code01, device_name03, device_type01, device_status01, device_address03,device_des03)]
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------异常场景测试数据-名称------------------------------------------------
name1 = '/名称'  # 以特殊字符开头
name2 = '12#$1' # 含有特殊字符
name3 = 'name123name名称123ASDname名namname名称123ASDname名称123ASDname名称123ASDname名称123ASDe名称123ASDname名称123ASD称 123ASDname名'  # 超过最大值--目前无最大值校验
name_abnormal_data1 = [(device_code03, name1, device_type01, device_status03, device_address01, device_des01),
                       (device_code03, name2, device_type01, device_status03, device_address01, device_des01)]
name_abnormal_data2 = [(device_code03, name3, device_type01, device_status03, device_address01, device_des01)]

edit_abnormal_data1 = [(name1,device_type02, device_status03, device_address01, device_des01),
                      (name2,device_type02, device_status03, device_address01, device_des01)]
edit_abnormal_data2 = [(name3,device_type02, device_status03, device_address01, device_des01)]
edit_abnormal_data3 = [(device_name02, device_type02, device_status03, device_address01,device_des01)]
# ------------------------------------------------------------------------------------------------------------------