# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageLotmg.py
# @中文描述 : 批次管理-page


from ElementApp.LotmgPage import *
from src.public.FunctionSet import *


# 进入批次管理界面
def login_lotmg():
    new_click(lotmg)
    new_click(lotmg_lotmg)

# 批次维护
def lot_maint(analysisdata, densitydata, potencydata):
    time.sleep(2)
    new_click(maintenance)
    time.sleep(2)
    new_click(resample)
    new_click(yes_primary)
    time.sleep(2)
    new_click(sample)
    new_click(yes_primary)
    time.sleep(2)
    ele = new_find_elements(analysis_density_potency)
    new_type_double_ele(ele[0], analysisdata)
    new_type_double_ele(ele[1], densitydata)
    new_type_double_ele(ele[2], potencydata)
    ele = new_find_elements(select)
    new_click_ele(ele[0])
    new_click(statusvalue)
    new_click_ele(ele[2])
    new_click(phavalue)
    new_click(yes)

# 锁定批次
def lot_locklot():
    new_click(locklot)
    new_click(yes_primary)

# 驳回批次
def lot_rejectlot():
    new_click(rejectlot)
    new_click(yes_primary)

# 锁定容器
def lot_lockcontainer(container):
    new_click(lockcon)
    ele = new_find_elements(containerid)
    new_send_keys_ele(ele[0], container)
    time.sleep(2)
    new_click(yes)

# 驳回容器
def lot_rejectcontainer(container):
    new_click(rejectcon)
    ele = new_find_elements(containerid)
    new_send_keys_ele(ele[0], container)
    time.sleep(2)
    new_click(yes)