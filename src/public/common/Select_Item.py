#coding=utf_8


from src.public.FunctionSet import *

# 选中某一选项
def select_item(selectitem):
    new_click('//*[text()="%s"]'%selectitem)
