#coding=utf-8

"""
Created on 2020/9/15
@author: lianxiujuan
@desc: 衡器校准页码元素
"""


# 进入衡器校准界面
weigh = '//*[text()="称量管理"]'
weighcal = '//*[text()="衡器校准"]'

# 衡器校准上端按钮
cal = '//span[text()="校准"]'
cert = '//span[text()="输入证书"]'

# 衡器校准界面元素
allselect = '//div[@class="layout con wrap"]//i[text()="arrow_drop_down"]'
firstscope = '//div[@role="listbox"]//div[text()="1"]'
firstcw = '//div[text()="校准砝码"]'
cleanyes = '//button[@color="primary"]'
calbutton = '//div[@class="layout con wrap"]//span[text()="校准"]'
cancelcalbutton = '//div[@class="layout con wrap"]//span[text()="取消校准"]'
# cancelcalyes = "//div[2]/button[2]/span"

# 输入证书页面元素
allinput = '//div[@class="v-card__text"]//input[@type="text"]'
addcert = '//*[text()="新增证书"]'
delecert = '//*[text()="删除证书"]'
currenttime = '//button[@class="v-btn v-btn--rounded v-btn--outlined theme--light accent--text"]//div[@class="v-btn__content"]'

close = '//span[text()="取消"]'
