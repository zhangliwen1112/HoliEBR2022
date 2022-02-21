# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageWeighset.py
# @中文描述 : 衡器设置-page


from ElementApp.WeighsetPage import *
from src.public.FunctionSet import *


# 进入衡器设置界面
def login_weighset():
    new_click(weigh)
    new_click(weighset)


# 新增衡器-无证书
def weighset_nocert_add(minvalue, maxvalue, offset, calerror):
    new_click(add)
    time.sleep(2)
    ele = new_find_elements(allselect)
    new_click_ele(ele[0])
    new_click(code)
    new_click_ele(ele[1])
    new_click(weightype)
    new_click_ele(ele[2])
    new_click(Mbrand)
    new_click_ele(ele[3])
    new_click(kg_unit)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[6], minvalue)
    new_send_keys_ele(ele[7], maxvalue)
    new_click_ele(ele[9])
    new_click(cwsele)
    new_click(cwyes)
    time.sleep(2)
    new_send_keys_ele(ele[13], maxvalue)
    new_send_keys_ele(ele[14], offset)
    new_send_keys_ele(ele[15], calerror)
    new_click(yes_button)


# 新增衡器-含证书
def weighset_withcert_add(minvalue, maxvalue, offset, calerror, certdays):
    new_click(add)
    time.sleep(2)
    ele = new_find_elements(allselect)
    new_click_ele(ele[0])
    sleep(2)
    new_click(code)
    sleep(1)
    new_click_ele(ele[1])
    new_click(weightype)
    new_click_ele(ele[2])
    new_click(Mbrand)
    new_click_ele(ele[3])
    new_click(kg_unit)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[6], minvalue)
    new_send_keys_ele(ele[7], maxvalue)
    new_click_ele(ele[9])
    new_click(cwsele)
    new_click(cwyes)
    time.sleep(2)
    new_click(cert)
    time.sleep(1)
    new_type_double_ele(ele[10], certdays)
    new_send_keys_ele(ele[13], maxvalue)
    new_send_keys_ele(ele[14], offset)
    new_send_keys_ele(ele[15], calerror)
    new_click(yes_button)


# 编辑衡器
def weighset_edit(minvalue, maxvalue, offset, calerror,certdays):
    new_click(edit)
    time.sleep(2)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[6], minvalue)
    new_type_double_ele(ele[7], maxvalue)
    new_click(cert)
    time.sleep(1)
    new_type_double_ele(ele[10], certdays)
    new_type_double_ele(ele[13], maxvalue)
    new_type_double_ele(ele[14], offset)
    new_type_double_ele(ele[15], calerror)
    new_click(yes_button)


# 删除衡器
def weighset_delete():
    new_click(delete)
    new_click(delete_yes_button)
