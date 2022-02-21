#coding=utf-8

"""
Created on 2021/1/14
@author: lianxiujuan
@desc: 批次接收
"""


lotmg = "//div[@class='v-list-item theme--light']//*[text()='批次管理']"
lotreceive = "//*[text()='批次接收']"

# 批次接收上端按钮
add = "//*[text()='新增']"
delete = "//*[text()='删除']"
cancel = "//*[text()='取消']"

# 批次接收-新增上端按钮
pack = "//*[text()='包装']"
approve = "//*[text()='核准']"
label = "//*[text()='标签']"
sample = "//*[text()='取样']"
store = "//*[text()='入库']"

# 新增界面元素
supply_material = '//div[@class="v-expansion-panel-content"]//div[@class="v-text-field__slot"]//input[@readonly="readonly"]'
supplysele = "//td/div/div"
supply_yes = "//div[3]/div/div[3]/button[1]"
supplylot = "//div[@id='app']/div/main/div/div/div/div//div/div/div[2]/div/form/div/div[2]/div/div/div/div[3]/div/div/div/div/input"
lot_qty = '//div[4]//div[3]//input'
materialsele = '//td[text()="lotreceive_code"]'
material_yes = "//div[4]/div/div[3]/button/span[contains(text(),'确定')]"
container_qty = "//div[3]/div/div/div[2]//div[2]/div/div/div/input"
# container_yes = "//div[@id='app']//main//div[2]/div[2]//div[3]/button[2]/span"
# add_yes = "//div[3]/div/div/div[3]/button[2]/span"
label_yes = '//div[4]/div/div/div[3]/button[2]/span'
close = '//div[3]/div/div/div[3]/button/span'
yes = '//span[text()="确定"]'
