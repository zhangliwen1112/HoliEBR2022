#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 设备管理-设备类别
"""


# 登录页码元素
device = '//div[@tabindex="-1"]//div[text()="设备管理"]'
deviceclass = '//div[text()="设备类别"]'

# 设备管理-设备类别上端按钮
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
copy = "//span[text()='复制']"
noeffect = "//span[text()='失效']"
effect = "//span[text()='生效']"

# 新增/编辑/复制类别界面元素
allinput = '//div[@class="container"]//input[@type="text"]'

yes_button = '//span[contains(text(), "确定")]'

other_yes_button = '//button[@color="primary"]//span[contains(text(), "确定")]'
