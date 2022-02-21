# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 13:39 
# @Author : 张丽雯 
# @File : WeightwoPage.py 
# @中文描述 :  称量工单页面元素

# 登录测试页面
weightmanage = "//*[contains(text(),'称量管理')]"
weigh_wo = "//*[contains(text(),'称量工单')]"

# 称量选项
gross_wo = "//*[text()='WO00000290']"
rmmix_wo = "//*[text()='WO00000290']"
weight_mode = "//div[@class='v-select__selections']"
net_mode = "//div[@class='v-list-item__title'][text()='净重']"
manual_mode = "//div[@class='v-list-item__title'][text()='人工输入']"
counting_mode = "//div[@class='v-list-item__title'][text()='计数']"
gross_mode = "//div[@class='v-list-item__title'][text()='毛重']"
rmmix_mode = "//div[@class='v-list-item__title'][text()='RM混合']"
containerID = "//div[@class='layout pt-2']//input[@type='text']"

# 容器列表界面
container_list = "//button/span[text()='容器列表']"
select_container = "//div[@class='container']//div[@role='row' and @aria-rowindex='2']" #选择第一行的容器
gross_container = '//*[text()="RL00000008 0001"]'
rmmix_container = '//*[text()="RL00000008 0001"]'
submit = "//span[text()='确定']"
verify = "//button/span[text()='验证']"
input_container = "//form/div[2]/div/div/div/div[1]/div/input"


# 称量过程信息
net = '//form/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input'   # 净重
tare = "//form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/input"    # 皮重
gross = '/html/body/div/div[1]/main/div/div/div/div/div[3]/div[1]/div/div[2]/div/' \
        'div[2]/div[2]/div/div[1]/div[1]/div/div[1]/form/div[3]/div[2]/div/div[3]/div/div/div[1]/div/input'   # 毛重
weightimes = '/html/body/div/div[1]/main/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]' \
             '/div/div/div[1]/div/div[1]/form/div[3]/div[1]/div/div[2]/div/div/div[1]/div/input'   # 称量次数
totalweigh = '/html/body/div/div[1]/main/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]' \
             '/div/div[1]/form/div[3]/div[1]/div/div[2]/div/div/div[1]/div/input'   # 总重量

# 清洁规则、危险信息弹框
message_alert = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']"

# 工单物料列表--n表示第几个物料，0,1,2... 表示第一个、第二个、第三个....
def material(n):
    return "//div[@class='layout column fill-height ma-0']//div[@row-index='"+n+"']//div[@aria-colindex='1']"

# 称量结果选择
weighFin = "//span[contains(.,'结束称量')]"
SamContainer = "//span[contains(.,'相同容器')]"
CanWeigh = "//span[contains(.,' 取消称量')]"

# 人工输入记录称量弹框
manual_submit = "//div[@class='v-card__actions']//span[contains(.,'确定')]"

# 剩余量
remain_number = "//form/div[3]/div[1]/div/div[1]/div/div/div[1]/div/input"
# 净重
net_number = "//form/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input"
# 皮重
tare_number = "//form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/input"
# 秤
weightvalue = "//div[@class='cp_precentage']/span"

# 批次信息
lot_detail = "//button/span[text()='批次信息']"
lot = "//tr[1]/td[2]"
container = "//tr[1]/td[4]"
closed = "//div[@class='v-card__actions']//span[contains(.,'关闭')]"

# 物料信息
mate_info = "//button/span[text()='物料信息']"
stage = '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]'
seq = '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]'
dose = '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[6]'

# 托盘标签
palletlabel = "//button/span[text()='托盘标签']"

# 取消称量
cancel_weight = "//button/span[text()='取消称量']"

# 界面右侧物料信息
material_msg = "//div/p[@class='text-truncate']"

# 强制称量
weighlist = "//span[text()='称量明细']"
waitweigh = "//div[text()='待称量']"
force_weigh = "//span[text()='强制称量']"

# 异常信息弹框
alert = "//div[@class='v-card v-sheet v-sheet--tile theme--light']"
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
no_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"
over_button = "//div[@class='DialogActions']//span[contains(.,'是')]"
nover_button = "//div[@class='DialogActions']//span[contains(.,'否')]"

yes = "//span[contains(.,'确定')]"
no = "//span[contains(.,'否')]"
