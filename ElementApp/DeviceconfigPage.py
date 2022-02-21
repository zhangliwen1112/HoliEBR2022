#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 设备管理-设备配置
"""


# 登录页码元素
device = '//div[@tabindex="-1"]//div[text()="设备管理"]'
deviceconfig = '//div[text()="设备配置"]'

# 设备管理-设备配置上端按钮
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
copy = "//span[text()='复制']"
noeffect = "//span[text()='失效']"
effect = "//span[text()='生效']"

# 新增/编辑/复制配置界面元素
allinput = "//div[@class='container']//input[@type='text']"
class1 = "//td[text()='表示混合容器的类型模板']"
classyes = "//div[@class='text-sm-right pt-2']//span[contains(text(),'确定')]"
yes_button = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[contains(text(),'确定')]"

# 失效/生效配置
other_yes_button = '//button[@color="primary"]//span[contains(text(), "确定")]'
