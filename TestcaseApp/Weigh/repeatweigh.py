#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 在MI中称量500次
"""


from ElementApp.MIexctPage import *
from src.public.FunctionSet import *
from src.public.common.Login import app_login
from selenium.webdriver.common.keys import Keys


def Repeatweigh():

    app_login('wang','1')

    # 进入MI执行界面
    new_click(manufacture)
    new_click(miexct)

    # 选择工单后选择物料
    new_click(wo)
    new_click(wo1)
    new_click(woyes)

    # 反复称量
    for i in range(500):
        new_click(containerlist)
        new_click(container1)
        new_click(yes)
        new_click(verify)
        new_click(yes)
        sleep(2)
        a=new_find_element(value)
        a.send_keys(Keys.CONTROL, 'a')
        new_click(no)



Repeatweigh()