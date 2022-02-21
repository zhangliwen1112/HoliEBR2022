#coding=utf-8
#
# """
# Created on 2020/9/14
# @author: lianxiujuan
# @desc: 校准设置
# """


# 登录页码元素
weigh = "//div[text()='称量管理']"
cal = "//div[text()='校准设置']"

# 界面信息
balance = "//div[contains(text(),'天平')]"
weighbridge = "//div[contains(text(),'地磅')]"
typeselect = "//i[@class='v-icon notranslate material-icons theme--light' and text()='arrow_drop_down']"
typecontent = "//div[text()='每半年']"
expires = "//input[@type='text' and @mask='#######']"
weightimes = "//input[@type='text' and @mask='######']"
save = "//span[text()='保存']"
step = "//textarea"

delete = "//div[@class='flex table']//i[text()='clear']"
yes_button = '//button[@color="primary"]//span[contains(text(), "确定")]'
