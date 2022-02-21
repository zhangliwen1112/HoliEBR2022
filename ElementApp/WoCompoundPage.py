# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 14:58 
# @Author : 张丽雯 
# @File : compoundingPage.py 
# @中文描述 :  集中混合

# 登录页码元素
workorder = "//*[contains(text(),'工单管理')]"
compounding = "//*[contains(text(),'工单集中')]"

#页面上的按钮元素
concentrate = "//span[contains(.,'集中')]"
compound = "//span[contains(.,'混合')]"
detail_button = "//span[contains(.,'明细')]"
refresh = "//span[contains(.,'刷新')]"

#集中页面元素
kucunID = "//div[3]/div/form/div/div/div/div/div/div/input"
concentrate_submit = '//form/div/div[2]/header/div/div/div/button/span'
reconcent = "//span[contains(.,'强行集中')]"
openconcent = "//span[contains(.,'开启集中')]"

relable = "//span[contains(.,'重新打印标签')]"
close = "//span[contains(.,'关闭')]"
#删除确定、取消
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

#混合页面元素
kuID = "//form/div/div/div/div/div/div/div/div/input"
overcontainer = "//form/div/div/div/div[3]/div/div/div/div/div"
compound_submit = "//span[contains(.,'提交')]"
recompound = "//span[contains(.,'强行混合')]"
opencompound = "//span[contains(.,'开启混合')]"
