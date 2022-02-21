# -*- coding: utf-8 -*- 
# @Time : 2021/1/21 9:40 
# @Author : 张丽雯 
# @File : pageDeviceManage.py 
# @中文描述 :  设备管理-设备管理界面

from ElementApp.DeviceManagePage import *
from src.public.common.Login import *


# 进入设备管理界面
def login_device_manage():
    new_click(device)
    new_click(device_manage)
    print('进入设备管理界面')


# 不可指派
def device_manage_unavailable(text):
    new_click(first_row)
    new_click(unavailable)
    new_type(comments, text)
    new_click(submit)


# 可指派
def device_manage_available(text):
    new_click(first_row)
    new_click(available)
    new_type(comments, text)
    new_click(submit)


# 手动
def device_manage_manual():
    new_click(first_row)
    new_click(manual)
    new_click(tips_submit)


# 自动
def device_manage_automatic():
    new_click(first_row)
    new_click(automatic)
    new_click(tips_submit)


# 离线
def device_manage_offline():
    new_click(first_row)
    new_click(offline)
    new_click(tips_submit)


# 上线
def device_manage_online():
    new_click(first_row)
    new_click(online)
    new_click(tips_submit)


# 标签
def device_manage_label(text):
    new_click(first_row)
    new_click(label)
    new_type(comments, text)
    new_click(submit)

# 指派
def device_manage_assign(text):
    new_click(first_row)
    new_click(assign)
    new_click(select_wo)
    new_click(select_wo1)
    new_click(select_wo_submit)
    new_type(comments, text)
    new_click(submit)

# 释放
def device_manage_release(text):
    new_click(first_row)
    new_click(release)
    new_type(comments, text)
    new_click(submit)

# 转移
def device_manage_transfer(text):
    new_click(first_row)
    new_click(transfer)
    new_type(comments, text)
    new_click(submit)

# 移动
def device_manage_move(text):
    new_click(first_row)
    new_click(move)
    new_type(comments, text)
    new_click(submit)

# 更新
def device_manage_update(text):
    new_click(first_row)
    new_click(update)
    new_type(comments, text)
    new_click(submit)

# 编辑
def device_manage_edit(text):
    new_click(first_row)
    new_click(edit)

    # 编辑分配状态
    new_click(assign_status)
    new_click(edit_edit)
    new_click(new_assignstatus_click)
    new_click(new_assignstatus)
    new_type(comments, text)
    new_click(submit)

    # 编辑Quantity
    new_click(edit_quantity)
    editedit = new_find_elements(edit_edit)
    new_click_ele(editedit[1])
    new_send_keys(new_quantity, 12)
    new_type(comments, text)
    new_click(submit)

    # 编辑assembled_with
    new_click(edit_assembledwith)
    editedit = new_find_elements(edit_edit)
    new_click_ele(editedit[1])
    new_send_keys(new_assembledwith, 12)
    new_type(comments, text)
    new_click(submit)

    # 编辑Declared_lot
    new_click(edit_declaredlot)
    editedit = new_find_elements(edit_edit)
    new_click_ele(editedit[1])
    new_send_keys(new_declaredlot, 12)
    new_type(comments, text)
    new_click(submit)

    # 编辑Declared_product
    new_click(edit_declaredproduct)
    editedit = new_find_elements(edit_edit)
    new_click_ele(editedit[1])
    new_send_keys(new_declaredproduct, 12)
    new_type(comments, text)
    new_click(submit)

    new_click(close_button)
