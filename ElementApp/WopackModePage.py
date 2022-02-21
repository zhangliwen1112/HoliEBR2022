# -*- coding: utf-8 -*- 
# @Time : 2021/1/7 13:47 
# @Author : 张丽雯 
# @File : workpackmode.py 
# @中文描述 :  产品包装方式

# 登录页码元素
workorder = "//*[contains(text(),'工单管理')]"
workpackmode = "//*[contains(text(),'产品包装方式')]"

# 按钮元素
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
delete = "//span[contains(.,'删除')]"
refresh = "//span[contains(.,'刷新')]"

# -------------------------------新增页面元素-----------------------------
# 物料
mater = "//form/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]/input"
# 选择第一个物料
mater_1 = "//tr[1]/td[1]/div/div"
mater_submit = "//div[@class='text-sm-right pt-2']//span[contains(.,'确定')]"

# 工作中心
station = "//form/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]"
# 选择第一个工作中心
station_1 = "//div/div[4]/div/div[2]/div[1]/table/tbody/tr/td[1]/div/div"
station_submit = "//*[@id='app']/div[4]/div/div[3]/button[1]/span"

# 包装信息
pack = "//div[@class='flex sm8']//input"
default = "//label[contains(.,'是否默认')]"
pallet = "//form/div/div/div[3]/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div[1]"
# 选择托盘类型P1 P2
pallet_P1 = "//div[@class='v-list-item__title'][contains(.,'P1')]"
pallet_P2 = "//div[@class='v-list-item__title'][contains(.,'P2')]"
pallet_tare = "//form/div/div/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div/input"
pallet_unit = "//form/div/div/div[3]/div/div/div/div/div/div[6]/div/div/div[1]/div[1]/div[1]"
unit_g = "//div[@class='v-list-item__title'][contains(.,'克')]"
unit_kg = "//div[@class='v-list-item__title'][contains(.,'千克')]"
# 选择容器
container = "//form/div/div/div[3]/div/div/div/div/div/div[8]/div/div/div[1]/div[1]/div[1]"
container_C1 = "//div[@class='v-list-item__title'][contains(.,'C1')]"
container_C2 = "//div[@class='v-list-item__title'][contains(.,'C2')]"
container_tare = "//form/div/div/div[3]/div/div/div/div/div/div[10]/div/div/div[1]/div/input"
container_unit = "//form/div/div/div[3]/div/div/div/div/div/div[11]/div/div/div[1]/div[1]/div[1]"
container_num = "//form/div/div/div[3]/div/div/div/div/div/div[14]/div/div/div[1]/div/input"

submit = "//span[contains(.,'确定')]"

#-----------------------------筛选-----------------------------------
search = "//span[contains(.,'筛选')]"
#按包装说明筛选
packinfo = "//span[@ref='eTitle'][contains(.,'包装说明')]"
packinfo_text = "//div[4]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"

#---------------------删除弹框确认、取消按钮元素-------------------------
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[contains(.,'取消')]"