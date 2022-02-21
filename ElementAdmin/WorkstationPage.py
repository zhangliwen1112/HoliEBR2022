#coding=utf-8

"""
Created on 2020/9/10
@author: lianxiujuan
@desc: 工作站
"""


# 登录工作站界面
workcenter = "//div[@class='menu-con']//span[text()='工作中心']"
worksta = "//span[text()='工作站']"

# 工作站界面中表格上端按钮
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
refresh = "//span[text()='刷新']"
delete = "//span[text()='删除']"

# 新增界面的元素
code = "//input[@placeholder='请输入编码']"
name = "//input[@placeholder='请输入名称']"
extdevice = "//i[@class='ivu-icon ivu-icon-ios-more']"
extdevice_all = "//div[@class='ivu-table-header']//input[@class='ivu-checkbox-input']"
yes_button = "//button[@class='ivu-btn ivu-btn-primary']//span[text()='确定']"   # 新增界面的确定和外部设备选项界面的确定公用此项
submit = "//div[@class='custom-width v-transfer-dom']//span[contains(text(),'确定')]"
# 删除界面
delete_yes_button = "//button[@class='ivu-btn ivu-btn-primary ivu-btn-small']//span[text()='确定']"
