#coding=utf-8

"""
Created on 2020/9/10
@author: lianxiujuan
@desc: OPC设置界面
"""


# 登录opc设置界面
syset = "//span[text()='系统设置']"
opcset = "//span[text()='OPC设置']"

# OPC设置界面中表格上端按钮
add = "//span[text()='新增']"
edit = "//button[@class='ivu-btn ivu-btn-default']//span[text()='编辑']"
delete = "//span[text()='删除']"
lock = "//span[text()='锁定']"
unlock = "//span[text()='解锁']"

# 新增/编辑界面的元素
name_code_address = "//input[@placeholder='请输入' and @class='ivu-input ivu-input-default']"
yes_button = "//div[@class='ivu-modal-footer']//span[text()='确定']"
cancel_button = "//div[@class='ivu-modal-footer']//span[contains(text(),'取消')]"

# 锁定/解锁/删除界面
other_yes_button = "//div[@class='ivu-poptip-footer']//span[text()='确定']"
