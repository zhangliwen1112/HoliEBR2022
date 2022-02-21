# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 9:27 
# @Author : 张丽雯 
# @File : pageWeightwo.py 
# @中文描述 :  称量工单-称量模式页面逻辑方法

from ElementApp.WeightwoPage import *
from ElementApp.WeightPage import weightmanage
from src.public.common.Login import *
from src.public.common.elements import *


# 进入称量工单页面
def login_weightwo():
    new_click(weightmanage)
    new_click(weigh_wo)
    print('进入称量工单页面')


# 净重称量模式
def weight_wo_net(n, tarevalue, selectmode='结束称量', isover='是'):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(net_mode)

    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)

    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    new_click(verify)
    sleep(1)
    if is_text_present('误差!衡器误差:'):
        sleep(2)
        new_click(yes_button)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(3)
    new_click(verify)
    sleep(1)
    if is_text_present('称量量已超出容器剩余量，确定要继续吗？'):
        new_click(yes_button)
        sleep(1)
    if selectmode == '结束称量':
        new_click(weighFin)
    elif selectmode == '相同容器':
        new_click(SamContainer)
    else:
        new_click(CanWeigh)
    sleep(2)
    if is_text_present('是否结束容器？'):
        if isover == '是':
            new_click(over_button)
        else:
            new_click(nover_button)
    sleep(2)

# 人工输入称量模式
def weight_wo_manual(n, netvalue, tarevalue):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(manual_mode)
    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(3)
    new_click(verify)
    sleep(1)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
        sleep(1)
    sleep(2)
    for i in range(1, 15):
        new_backspace(net)
    new_type(net, netvalue)
    sleep(2)
    new_click(net)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(2)
    if is_text_present('记录称量'):
        sleep(1)
        new_click(manual_submit)
    sleep(2)


# 计数称量模式
def weight_wo_count(n, tarevalue, isover='是'):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(counting_mode)
    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(3)
    new_click(verify)
    sleep(1)
    if is_text_present('误差!衡器误差:'):
        sleep(1)
        new_click(yes_button)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
        sleep(1)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(2)
    new_click(verify)
    sleep(1)
    if is_text_present('记录称量'):
        sleep(1)
        new_click(manual_submit)
    sleep(1)
    if is_text_present('是否结束容器？'):
        if isover == '是':
            new_click(over_button)
        else:
            new_click(nover_button)
    sleep(2)

# 批次信息
def weight_wo_lot_detail(n):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    # 通过容器列表选择
    new_click(container_list)
    sleep(0.5)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    new_click(lot_detail)
    if new_get_text(container) == new_js_text(input_container):
        print('批次信息容器号是：', new_get_text(container))
    else:
        print('批次信息容器号不正确！')
    if new_get_text(lot) == new_js_text(input_container)[:-5]:
        print('批次信息批次号是：', new_get_text(lot))
    else:
        print('批次信息批次号不正确！')
    sleep(2)
    new_click(closed)


# 取消称量
def weight_wo_cancel(n,cancelweight1='否',cancelweight2='否'):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    # 通过容器列表选择
    new_click(container_list)
    sleep(0.5)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    if cancelweight1 == '取消称量':
        new_click(cancel_weight)
    else:
        new_click(verify)
        sleep(1)
        if is_text_present('误差!衡器误差:'):
            sleep(1)
            new_click(yes_button)
        while is_element_present(message_alert):
            sleep(1)
            new_click(submit)
            sleep(1)
        new_click(verify)
        if cancelweight2 == '取消称量':
            new_click(cancel_weight)


def weight_wo_container_ID(ID):
    new_type(containerID,ID)
    new_click(material_msg)


# 强制称量
def forceweigh():
    new_click(weighlist)
    new_click(waitweigh)
    new_click(force_weigh)
    ele = new_find_elements(yes)
    new_click_ele(ele[1])

# 毛重模式称量
def grossweighmode(taredata):
    sleep(2)
    new_click(gross_wo)
    new_click(weight_mode)
    new_click(gross_mode)
    new_click(container_list)
    new_click(gross_container)
    new_click(yes)
    new_click(verify)
    sleep(2)
    new_click(yes)
    new_click(yes)
    sleep(2)
    new_type_double(tare, taredata)
    sleep(1)
    new_click(verify)
    sleep(1)
    new_click(verify)
    sleep(2)
    new_click(weighFin)
    sleep(3)
    new_click(no)

# 毛重模式称量，异常场景
def grossweighmode_abnormal(taredata):
    sleep(2)
    new_click(gross_wo)
    new_click(weight_mode)
    new_click(gross_mode)
    new_click(container_list)
    new_click(gross_container)
    new_click(yes)
    new_click(verify)
    sleep(2)
    new_click(yes)
    new_click(yes)
    sleep(2)
    new_type_double(tare, taredata)

# 毛重模式称量，截至至“结束称量”前
def grossweighmode2(taredata):
    sleep(2)
    new_click(gross_wo)
    new_click(weight_mode)
    new_click(gross_mode)
    new_click(container_list)
    new_click(gross_container)
    new_click(yes)
    new_click(verify)
    sleep(2)
    new_click(yes)
    new_click(yes)
    sleep(2)
    new_type_double(tare, taredata)
    sleep(1)
    new_click(verify)
    sleep(1)
    new_click(verify)
    sleep(2)

# rm模式称量
def rmweighmode(taredata):
    sleep(2)
    new_click(rmmix_wo)
    new_click(weight_mode)
    new_click(rmmix_mode)
    new_click(container_list)
    new_click(rmmix_container)
    new_click(yes)
    new_click(verify)
    sleep(2)
    new_click(yes)
    sleep(2)
    new_type_double(tare, taredata)
    sleep(1)
    new_click(verify)
    sleep(1)
    new_click(verify)
    sleep(2)
    new_click(weighFin)
    sleep(3)
    new_click(no)

# rm模式称量
def rmweighmode_abnormal(taredata):
    sleep(2)
    new_click(rmmix_wo)
    new_click(weight_mode)
    new_click(rmmix_mode)
    new_click(container_list)
    new_click(rmmix_container)
    new_click(yes)
    new_click(verify)
    sleep(2)
    new_click(yes)
    sleep(2)
    new_type_double(tare, taredata)

# 物料信息
def material_info():
    sleep(2)
    new_click(mate_info)

# 托盘标签
def pallet_label():
    sleep(2)
    new_click(container_list)
    new_click(gross_container)
    new_click(yes)
    new_click(palletlabel)

# 净重称量-获取净重值
def weight_wo_net_netvalue(n, tarevalue):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(net_mode)

    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)

    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    new_click(verify)
    sleep(1)
    if is_text_present('误差!衡器误差:'):
        sleep(2)
        new_click(yes_button)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(3)
    new_click(verify)
    sleep(2)
    net_value = new_js_text(net_number)
    print(net_value)
    tare_value = new_js_text(tare_number)
    print(tare_value)