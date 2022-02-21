# -*- coding: utf-8 -*- 
# @Time : 2021/1/21 9:41 
# @Author : 张丽雯 
# @File : DeviceManagePage.py 
# @中文描述 :  设备管理-设备管理页面元素

# 登录页码元素
device = "//*[contains(text(),'设备管理')]"
device_manage = "//div[@class='v-list-group__items']//*[contains(text(),'设备管理')]"

# 列表上端按钮
assign = "//span[text()='指派']"
available = "//span[text()='可指派']"
unavailable = "//span[text()='不可指派']"
release = "//span[text()='释放']"
move = "//span[text()='移动']"
transfer = "//span[text()='转移']"
online = "//span[text()='上线']"
offline = "//span[text()='离线']"
edit = "//span[contains(.,'编辑')]"
automatic = "//span[text()='自动']"
manual = "//span[text()='手动']"
update = "//span[text()='更新']"
label = "//span[text()='标签']"
check = "//span[text()='查看']"
refresh = "//span[text()='刷新']"

# -----------------------------------------指派页面元素------------------------------------------
select_wo = "//input[@readonly='readonly']"
select_wo1 = "//tbody//tr[1]"  #选择第一个工单
select_wo_submit = "//div[@class='text-sm-right pt-2']//span[text()='确定']"

# -----------------------------------------备注、提交按钮元素（指派页面、转移等页面均一样）--------------------------------------
first_row = "//span[@ref='eCellValue'][text()='1']"   #选择第一行，序号为1
comments = "//textarea"
submit = "//span[text()='确定']"
tips_submit = "//div[@class='DialogActions']//span[contains(.,'确定')]"  #弹框确定按钮


# -----------------------------------------编辑界面元素--------------------------------------
edit_edit = "//div[@class='v-card v-sheet theme--light']//span[text()='编辑']"
# 分配状态参数
assign_status = "//div[text()='分配状态']"

new_assignstatus_click = '//div[@class="row"]//i[text()="arrow_drop_down"]'
new_assignstatus = '//div[@tabindex="0" and @role="option"]//div[text()="AVAILABLE"]'

# Quantity参数
edit_quantity = '//div[text()="QUANTITY"]'
new_quantity = '//div[@class="row"]//div[@class="col"]/div[@class="v-input v-input--has-' \
               'state theme--light v-text-field v-text-field--is-booted error--text"]'

# assembled_with参数
edit_assembledwith = '//div[text()="ASSEMBLED_WITH"]'
new_assembledwith = '//div[@class="row"]//div[@class="col"]/div[@class="v-input v-input--' \
                    'has-state theme--light v-text-field v-text-field--is-booted error--text"]'

# declared_lot参数
edit_declaredlot = '//div[text()="DECLARED_LOT"]'
new_declaredlot = '//div[@class="row"]//div[@class="col"]/div[@class="v-input v-input--has-' \
                  'state theme--light v-text-field v-text-field--is-booted error--text"]'

# declared_product参数
edit_declaredproduct = '//div[text()="DECLARED_PRODUCT"]'
new_declaredproduct = '//div[@class="row"]//div[@class="col"]/div[@class="v-input v-input--' \
                      'has-state theme--light v-text-field v-text-field--is-booted error--text"]'

close_button = "//span[text()='关闭']"
