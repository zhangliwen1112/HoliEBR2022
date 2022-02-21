# -*- coding: utf-8 -*- 
# @Time : 2021/1/12 10:21 
# @Author : 张丽雯 
# @File : MIexecutionPage.py
# @中文描述 :  MI执行--关联的MI为gongxu

# 登录页码元素
manufacture = "//*[contains(text(),'生产管理')]"
MIexecution = "//*[contains(text(),'MI执行')]"

# MI执行上端按钮
wo = "//div[@id='mi-excute-layout']/div/div/div/div/div/div/input"
wo1 = "//td/div/div"
woyes = "//div[3]/div/div[3]/button/span"
start = "//span[contains(.,'kaishi')]"

# ------------------------------------组件元素----------------------------------
# upload上传文件
upload = "//input[@type='file']"
next1 = "//i[text()='arrow_forward']"

# text文本框
text = "//div[6]/div/div[2]/form/div/div/div[1]/div/input"

# 多行文本
multi = "//textarea"

# 数字
num = "//input[@type='number']"

# 多选框
multiselect = "//div[@class='v-input--selection-controls__input']"

# 签名
sign = "//span[contains(.,'签名')]"
user = "//input[@autocomplete='new-password' and @type='text']"
pwd = "//input[@autocomplete='new-password' and @type='password']"
sign_yes = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[text()='确定']"

# 强制执行
force = "//div[17]/div/div[2]/div/div/div[1]/div/input"

# 警示
alert_type = "//form/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]"
errors = "//div[text()='偏差']"
notes = "//div[text()='备注']"
alert_level = "//form/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]"
none = "//div[text()='无']"
small = "//div[text()='微小']"
major = "//div[text()='重要']"
serious = "//div[text()='严重']"
alert_text = "//div[18]/div/div[2]/form/div/div[2]/div/div/div[1]/div/input"

#快速称量
scale = "//i[@title='称量']"
scale_yes = "//span[text()='验证']"
