#coding=utf_8


from src.public.FunctionSet import *

# ѡ��ĳһѡ��
def select_item(selectitem):
    new_click('//*[text()="%s"]'%selectitem)
