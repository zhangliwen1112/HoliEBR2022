#coding=utf-8

"""
Created on 2020/9/15
@author: lianxiujuan
@desc: 衡器设置页码元素
"""


# 进入衡器设置界面
weigh = '//*[text()="称量管理"]'
weighset = '//*[text()="衡器设置"]'

# 衡器设置上端按钮
add ='//*[text()="新增"]'
edit = '//*[text()="编辑"]'
delete = '//*[text()="删除"]'

# 新增/编辑衡器设置界面元素
allselect = '//div[@class="v-card v-sheet theme--light"]//i[text()="arrow_drop_down"]'
code = '//div[text()="aaa"]'
weightype = '//div[@class="v-select-list v-card theme--light"]//div[text()="天平"]'
Mbrand = '//div[text()="METTLER"]'
kg_unit = '//div[@class="v-select-list v-card theme--light"]//div[text()="kg"]'
allinput = '//div[@class="v-card v-sheet theme--light"]//input[@type="text"]'
cwsele = "//th/div/div"
cwyes = '//div[@class="text-sm-right pt-2"]//span[contains(text(),"确定")]'
cert = '//div[@class="v-input--selection-controls__ripple"]'
yes_button = '//div[@class="v-card v-sheet theme--light"]//span[text()="确定"]'
cancel_button = '//div[@class="v-card v-sheet theme--light"]//span[text()="取消"]'

# 删除衡器设置
delete_yes_button = '//*[@color="red"]//*[contains(text(),"确定")]'
