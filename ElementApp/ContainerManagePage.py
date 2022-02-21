# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 15:24 
# @Author : 张丽雯 
# @File : ContainerManage.py 
# @中文描述 :  容器管理界面

# 登录页码元素
inventory = "//*[contains(text(),'库存管理')]"
container = "//*[contains(text(),'容器')]"
containermanage = "//*[contains(text(),'容器管理')]"

# 标准容器上端按钮
detail = "//span[contains(.,'明细')]"
status = "//span[contains(.,'状态')]"
move = "//span[contains(.,'移动')]"
reback = "//span[contains(.,'返回')]"
split = "//span[contains(.,'拆分')]"
label = "//span[contains(.,'标签重打')]"
refresh = "//span[contains(.,'刷新')]"

# 第一个容器
first_container = "//div[@role= 'row' and @row-index='0']/div[@col-id='0']"

# -------------------------------明细界面元素--------------------------------
open = "//div[@class='v-select__selections']"
open_Y = "//div[@class='v-list-item__content'][contains(.,'Y')]"
open_N = "//div[@class='v-list-item__content'][contains(.,'N')]"
pallet_detail = "//button[contains(.,'托盘明细')]"
submit = "//button[contains(.,'确定')]"
cancel = "//button[contains(.,'取消')]"
# 托盘明细小标题
entity = "//button[contains(.,'实体')]"
receive = "//button[contains(.,'接收')]"
storage = "//button[contains(.,'库位')]"
container_list = "//button[contains(.,'容器列表')]"
close = "//button[contains(.,'关闭')]"

# -------------------------------------移动界面元素------------------------------------
# 选择第一个库位
target_storage = "//div[@class='v-card__text']//div[@class='ag-center-cols-container']//div[@role='row' and @row-index='0']"
# 库位不兼容
submit1 = "//main/div/div/div/div/div[2]/div[3]/div/div/div[3]/button[2]/span"

# -------------------------------------拆分界面元素------------------------------------
split_type1 = "//label[contains(.,'原托盘')]"
split_type2 = "//label[contains(.,'新容器')]"
input_type1 = "//label[contains(.,'手动录入')]"
input_type2 = "//label[contains(.,'称量')]"
split_num = "//form/div/div/div[27]/div/div/div[1]/div/input"

# ------------------------------------标签打印页面元素-----------------------------------
print_num = '//div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div/div[1]/div/input'

# ------------------------------------状态页面元素---------------------------------------
select_status = "//div[@class='v-select__selections']"
status1 = "//div[@class='v-list-item__title'][contains(.,'锁定')]"
status2 = "//div[@class='v-list-item__title'][contains(.,'驳回')]"

# ------------------------------------筛选(按容器状态筛选)----------------------------------------------
search = "//span[contains(.,'筛选')]"
Cstatus = "//span[@ref='eTitle'][contains(.,'容器状态')]"
select = "//select[@id='filterText']"
reject = "//option[contains(.,'驳回')]"
locking = "//option[contains(.,'锁定')]"
# 搜索后选择第一行
first_row = "//div[@class='ag-center-cols-container']"






