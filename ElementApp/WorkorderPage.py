#coding=utf-8

"""
Created on 2020/9/14
@author: lianxiujuan
@desc: 工单管理
"""


# 登录页码元素
workorder = "//*[text()='工单管理']"
aworkorder = '//a[@tabindex="0"]//*[text()="工单管理"]'

# 工单管理上端按钮
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
modify = "//span[text()='修订']"
copy = "//span[text()='复制']"
release = "//span[text()='发布']"
cancelre = "//span[text()='撤销发布']"
cancel = "//span[text()='取消']"
stop = "//span[text()='终止']"
close = "//span[text()='关闭']"

# 新增/编辑/修订工单界面元素
formula = '//div[@class="v-card v-sheet theme--light"]//input[@type="text" and @readonly="readonly"]'
formulasele = '//td/div/div'
formulayes = "//div[@class='text-sm-right pt-2']//span[contains(.,'确定')]"
qty = '//div[@class="v-card v-sheet theme--light"]//input[@name="qty"]'
yes_button = "//span[text()='确定']"
cancel_button = '//button[@class="v-btn v-btn--contained theme--light v-size--default"]//span[text()="取消"]'
type = "//div[@class='v-select__selections']//div[text()='生产工单']"
type_produce = "//div[@role='listbox']//div[text()='生产工单']"
type_weight = "//div[@role='listbox']//div[text()='称量工单']"
type_pack = "//div[@role='listbox']//div[text()='包装工单']"
type_other = "//div[@role='listbox']//div[text()='其他工单']"

# 修订工单
womaterial = "//div[text()='物料信息']"
firstmaterial = "//div[3]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]"
allqty = '//div[2]/div/div/div/div[2]/div/div/div/div/form/div/div/div[6]/div/div/div/div/div/div/input'
weight = "//label[text()='称量间称量']"
room = "//label[text()='车间称量']"
packing = "//label[text()='包装间称量']"
save = "//span[text()='保存']"

# 发布工单
re_input = '//form[@class="v-form"]//div[@class="layout row wrap"]//input[@readonly="readonly" and @type="text"]'
workcentersele = "//th//div//div"
workcenteryes = '//div[@class="v-card v-sheet theme--light"]//span[contains(text(),"确定")]'
misele = '//td[text()="demo1"]'
miyes = '//div[@class="v-menu__content theme--light v-menu__content--fixed' \
        ' menuable__content__active "]//span[text()="确定"]'
re_yes_button = '//div[@class="v-dialog v-dialog--active v-dialog--persistent ' \
                'v-dialog--scrollable"]//span[text()="确定"]'
# 工单
workcenter = "//div[2]/form/div/div/div[8]/div[1]/div/div[1]/div[1]/input"
workcentersele1 = "//div[5]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]"
workcenter_submit1 = "//div[5]/div/div[3]/button[1]"
mi1 = "//div[2]/div[3]/div/div/div[2]/form/div/div/div[9]/div[1]/div/div[1]/div[1]/input"
mi_select1 = "//div[6]/div/div[1]/div/div/div[1]/input"
misele1 = "//div[6]/div/div[2]/div[1]/table/tbody/tr/td[1]/div/div"
miyes1 = "//div[6]/div/div[3]/button[1]/span"
re_yes_button1 = "//div[3]/div/div/div[3]/button[2]/span"

# 取消、终止、关闭工单
other_yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
