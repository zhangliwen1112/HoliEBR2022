# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageWeighcal.py
# @中文描述 : 衡器校准-page


from ElementApp.WeighcalPage import *
from src.public.FunctionSet import *


# 进入衡器校准界面
def login_weighcal():
    new_click(weigh)
    new_click(weighcal)

# 校准
def weighcal_cal():
    new_click(cal)
    time.sleep(2)
    ele = new_find_elements(allselect)
    new_click_ele(ele[1])
    new_click(firstscope)
    new_click_ele(ele[2])
    new_click(firstcw)
    new_click(calbutton)
    new_click(cleanyes)
    new_click(calbutton)
    new_click(close)

# 证书
def weighcal_cert():
    new_click(cert)
    time.sleep(2)
    ele = new_find_elements(allinput)
    "#input-2193"
    "document.querySelector('#input-2193')"
    js = "document.getElementById('').value='{}'".format("2029-2-10")
    driver.execute_script(js)
    new_send_keys_ele(ele[0], '2029-2-10')
    new_send_keys_ele(ele[1], '2055-2-10')
    new_send_keys_ele(ele[2], 'urllib3介绍')
    new_click(addcert)
    time.sleep(1)
    new_click(delecert)
    new_click(close)
