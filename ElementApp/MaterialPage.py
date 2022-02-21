#coding=utf-8

"""
Created on 2020/9/14
@author: lianxiujuan
@desc: 物料管理
"""


# 登录页码元素
material = '//div[@class="v-list-item theme--light"]//div[text()="物料管理"]'
amaterial = '//div[@class="v-list-group__items"]//div[text()="物料管理"]'

# 物料管理上端按钮
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
copy = "//span[text()='复制']"
verify = "//span[text()='验证']"
cancelverify = "//span[text()='取消验证']"
noeffect = "//span[text()='失效']"
effect = "//span[text()='生效']"

# 新增/编辑/复制物料界面元素
allinput = '//form[@id="materialContent"]//input[@type="text"]'
desc = '//textarea'

yes_button = '//div[@class="v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable"]//span[text()="确定"]'
cancel_button = '//div[@class="v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable"]//span[text()="取消"]'

# 验证物料
other_yes_button = '//button[@color="primary"]//span[contains(text(),"确定")]'
