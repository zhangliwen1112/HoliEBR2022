# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 10:21 
# @Author : 张丽雯 
# @File : DeclarationPage.py 
# @中文描述 :  生产声明

# 登录页码元素
workorder = "//*[contains(text(),'工单管理')]"
Declaration = "//*[contains(text(),'生产声明')]"

#页面上的按钮元素
declaration_button = "//span[contains(.,'生产声明')]"
prelabel_button = "//span[contains(.,'预标签')]"
relabel_button = "//span[contains(.,'重标签')]"
woreject_button  = "//span[contains(.,'拒绝声明')]"
woreuse_button = "//span[contains(.,'重用声明')]"
detail_button = "//span[contains(.,'声明明细')]"
refresh = "//span[contains(.,'刷新')]"

#生产声明-声明页面元素
declara_num = "//div[2]/div/div/div/div/div/div/div/div[8]/div/div/div/div/input"
palletType = "//form/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div/input"
palletType1 = "//body/div/div[3]/div/div/div/div[2]/div"
containerNumber = "//div[3]/div/div/div/div/div/div[5]/div/div/div/div/input"
kuqu = "//div[5]/div/div/div/div/div/div[2]/div/div/div/div/input"
kuqu1 = "//td/div/div"
kuqu_submit = "//div[4]/div/div[3]/button[1]"
kuwei = "//div[5]/div/div/div/div/div/div[3]/div/div/div/div/input"
kuwei1 = "//div[5]/div/div[2]/div[1]/table/tbody/tr/td[1]/div/div"
kuwei_submit = "//div[5]/div/div[3]/button[1]"
submit = "//body/div/div[1]/main/div/div/div/div/div[2]/div[3]/div/div/div[3]/button[2]"

#展开、折叠小标签
pallettitle = "//button[contains(text(),'托盘')]"
containertitle = "//button[contains(text(),'容器')]"
labletitle = "//button[contains(text(),'标签信息')]"

# 弹框确定元素
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"

