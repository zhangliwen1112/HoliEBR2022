#coding=utf-8
#
# """
# Created on 2020/9/14
# @author: zhangliwen
# @desc:
# """
# from .base import Page
from selenium.webdriver.common.by import By
"""
工作中心-外部设备页面对象定义
"""

# 进入页面 xpath
Work_Centre = "//*[contains(text(),'工作中心')]"
Device_Page = "//*[contains(text(),'外部设备')]"


#页面上面按钮
add = '//*[contains(text(),"新增")]'
delete = '//*[contains(text(),"删除")]'
edit = '//*[contains(text(),"编辑")]'
fresh = '//*[contains(text(),"刷新")]'
show = "//span[contains(.,'显示列')]"
select = "//span[contains(.,'筛选')]"

#新增页面元素
code = "//input[@placeholder='请输入编码']"
name = "//input[@placeholder='请输入名称']"
type = "//div[@placeholder='请选择设备类型']"
type1 = "//li[contains(.,'打印机')]"
type2 = "//li[contains(.,'电子秤')]"
type3 = "//li[contains(.,'手环')]"
status = "//div[@placeholder='请选择状态']"
status1 = "//li[contains(.,'注册')]"
status2 = "//li[contains(.,'注销')]"
status3 = "//li[contains(.,'在线')]"
status4 = "//li[contains(.,'离线')]"
adr = "//input[@placeholder='请输入设备地址']"
worker = "//button[@class='ivu-btn ivu-btn-default ivu-btn-icon-only']"
worker_all = "//input[@class='ivu-checkbox-input']"
worker_submit = "//button[1]/span[text()='确定']"
des = "//textarea[@placeholder='请输入描述']"
submit = "//div[@class='custom-width v-transfer-dom']//span[contains(text(),'确定')]"
cancel = "//div[@class='custom-width v-transfer-dom']//span[contains(text(),'取消')]"
#删除确定取消按钮
delete_submit = "//button[@type='button']/span[text()='确定']"
delete_cancel = "//button[@type='button']/span[text()='取消']"

#筛选,第一个过滤条件
select1 = "//span[@ref='eTitle'][text()='编码']"
select1_text1 = "//input[@ref='eInput' and @placeholder='过滤条件...']"

#选中第一条
First = "//div[@role=\"row\" and @row-index=\"0\"]"

