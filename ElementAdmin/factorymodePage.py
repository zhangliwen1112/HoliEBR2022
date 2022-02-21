#coding=utf-8
#
# """
# Created on 2020/9/7
# @author: zhangliwen
# @desc:工厂模型模块，包括企业、厂区、区域、区段、位置
# """
# from .base import Page
from selenium.webdriver.common.by import By
"""
工厂模型-区域管理页面对象定义
"""

# 进入页面 xpath
Factory_Mode = "//*[contains(text(),'工厂模型')]"
Location_Manage = "//*[contains(text(),'位置管理')]"
Section_Manage = "//*[contains(text(),'区段管理')]"
Area_Manage = "//*[contains(text(),'区域管理')]"
Factory_Manage = "//*[contains(text(),'厂区管理')]"
Company_Manage = "//*[contains(text(),'企业管理')]"

#页面上面按钮
add = '//*[contains(text(),"新增")]'
delete = '//*[contains(text(),"删除")]'
edit = '//*[contains(text(),"编辑")]'
fresh = '//*[contains(text(),"刷新")]'
tag = '//*[contains(text(),"标签")]'
ralated = '//*[contains(text(),"关联")]'
show = "//span[contains(.,'显示列')]"
select = "//span[contains(.,'筛选')]"



#选中第一条
First = "//div[@role=\"row\" and @row-index=\"0\"]"

# ----------------------------新增、关联页面确定按钮------------------------
submit = "//div[@class='custom-width v-transfer-dom']//span[contains(text(),'确定')]"
cancel = "//div[@class='custom-width v-transfer-dom']//span[contains(text(),'取消')]"
#删除确定取消按钮
delete_submit = "//button[@type='button']/span[text()='确定']"
delete_cancel = "//button[@type='button']/span[text()='取消']"

#移动
movefirst = "//div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div"  #选中右侧第一个
removefirst = "//div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div" #选中左侧第一个
moveleft = "//b[contains(.,'<')]"
moveright = "//b[contains(.,'>')]"



#  -------------------------------位置、区域、企业、厂区管理编码、名称元素---------------------------------

Code = "//input[@placeholder='请输入编码']"
Name = "//input[@placeholder='请输入名称']"

#----------------------------------厂区管理-------------------------------------
#新增页面元素
Factory_Adr1 = "//input[@placeholder='请输入地址一']"
Factory_Adr2 = "//input[@placeholder='请输入地址二']"
Factory_Adr3 = "//input[@placeholder='请输入地址三']"
Factory_Adr4 = "//input[@placeholder='请输入地址四']"


#------------------------------区段管理--------------------------------------------
#区段管理新增弹框元素
section_type="//span[@class='ivu-select-selected-value']"
section_type1= "//li[text()='生产']"    #生产
section_type2 = "//li[contains(.,'仓库')]"   #仓库
store_type = "//span[@class='ivu-select-placeholder']"
store_type1 = "//li[contains(.,'原材料')]"
store_type2 = "//li[contains(.,'半成品')]"
store_type3 = "//li[contains(.,'包材')]"
store_type4 = "//li[contains(.,'成品')]"

#筛选,第一个过滤条件
select_code = "//span[@ref='eTitle'][text()='编码']"
select1_text1 = "//input[@ref='eInput' and @placeholder='过滤条件...']"


