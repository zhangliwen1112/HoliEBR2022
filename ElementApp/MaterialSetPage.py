# -*- coding: utf-8 -*- 
# @Time : 2021/1/13 16:12 
# @Author : 张丽雯 
# @File : MaterialSetPage.py 
# @中文描述 :  物料字段设置界面

# 登录页码元素
material = "//*[contains(text(),'物料管理')]"
materialset = "//*[contains(text(),'物料属性设置')]"

# 物料字段设置上端按钮
edit = "//span[contains(.,'编辑')]"
default = "//span[contains(.,'默认值设置')]"
refresh = "//span[contains(.,'刷新')]"

# -----------------------------编辑页面元素-----------------------------
isMandatory = "//label[text()='是否必填']"
isImpactValidation = "//label[text()='是否影响验证']"
isFromERP = "//label[text()='是否来自ERP']"
isselect = "//form//div[@class='v-input--selection-controls__input']//input"
yes_button = "//span[text()='确定']"
no_button = "//span[text()='取消']"

# -----------------------------默认值设置页面元素-----------------------------
# 描述
desc = "//textarea[@rows='2']"
# 基础信息
family = "//div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/input"
EC = "//form/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/input"
type = "//div[2]/div[1]/div/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div"
type1 = "//div[@role='listbox']//div[text()='原材料']"
type2 = "//div[@role='listbox']//div[text()='半成品']"
type3 = "//div[@role='listbox']//div[text()='包材']"
type4 = "//div[@role='listbox']//div[text()='成品']"
unit = "//div[2]/div[1]/div/div/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/div[1]"
mg = "//div[@role='listbox']//div[text()='mg']"
g = "//div[@role='listbox']//div[text()='g']"
kg = "//div[@role='listbox']//div[text()='kg']"
lb = "//div[@role='listbox']//div[text()='lb']"
l = "//div[@role='listbox']//div[text()='l']"
ml = "//div[@role='listbox']//div[text()='ml']"
fl = "//div[@role='listbox']//div[text()='fl']"
un = "//div[@role='listbox']//div[text()='un']"
kn = "//div[@role='listbox']//div[text()='kn']"
potency = "//form/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]"
N = "//div[@role='listbox']//div[text()='无效价  N']"
P = "//div[@role='listbox']//div[text()='%  P']"
L = "//div[@role='listbox']//div[text()='μg/mg  L']"
U = "//div[@role='listbox']//div[text()='iu/mg  U']"
M = "//div[@role='listbox']//div[text()='mu/g   M']"
R = "//div[@role='listbox']//div[text()='μg/ml  R']"
S = "//div[@role='listbox']//div[text()='mg/ml  S']"
T = "//div[@role='listbox']//div[text()='iu/ml  T']"
V = "//div[@role='listbox']//div[text()='iu/g   V']"
info_title = "//button[contains(.,' 主要')]"

# 公共元素
input_text = "//div[@class='v-card v-sheet theme--light']//div[@class='v-text-field__slot']//input"
select = "//div[@class='v-select__selection v-select__selection--comma']"

# 称量信息
error_message = "//div[@class='v-messages__message message-transition-enter-to']"
weight_mode = '//*[@id="materialContent"]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]'
net = "//div[@role='listbox']//div[text()='净重']"
gross = "//div[@role='listbox']//div[text()='毛重']"
manual = "//div[@role='listbox']//div[text()='人工输入']"
weight_title = "//button[contains(.,' 称量')]"

# 批次信息
validity = "//form/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/input"
validity_unit = "//form/div[2]/div[3]/div/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div"
validity_day = "//div[@role='listbox']//div[text()='日']"
validity_month = "//div[@role='listbox']//div[text()='月']"
validity_alarm = "//form/div[2]/div[3]/div/div/div[1]/div[2]/div[4]/div/div/div[1]/div/input"
sample_qty = "//form/div[2]/div[3]/div/div/div[1]/div[2]/div[5]/div/div/div[1]/div/input"
lot_title = "//button[contains(.,' 批次/存储')]"
# 区域信息
default_pallet = "//form/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]"
default_pallet1 = "//body/div/div[8]/div/div/div/div/div"
default_container = "//form/div[2]/div[3]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]"
# default_container1 = "//div[@role='listbox']//div[text()='3333']"
default_container1 = "//body/div/div[9]/div/div/div/div/div"
backup_pallet = "//*[@id='materialContent']/div[2]/div[3]/div/div/div[3]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]"
# backup_pallet1 = "//div[@role='listbox']//div[text()='2222']"
backup_pallet1 = "//body/div/div[10]/div/div/div/div/div"
backup_container = "//*[@id='materialContent']/div[2]/div[3]/div/div/div[3]/div[2]/div[4]/div/div/div[1]/div[1]/div[1]"
# backup_container1 = "//div[@role='listbox']//div[text()='4444']"
backup_container1 = "//body/div/div[11]/div/div/div/div/div"

# 取样信息
sample_init = "//*[@id='materialContent']/div[2]/div[3]/div/div/div[4]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]"
# sample_init1 = "//div[@role='listbox']//div[text()='bbbb']"
sample_init1 = "//body/div/div[12]/div/div/div/div/div"
sample_zone = "//*[@id='materialContent']/div[2]/div[3]/div/div/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]"
sample_zone1 = "//body/div/div[13]/div/div/div[1]/div/div"
sample_rule = "//form/div[2]/div[3]/div/div/div[4]/div[3]/div/div[1]/div/div[1]/div[1]/input"
sample_A = "//td[contains(.,'每件取样贴标:')]"
sample_C = "//td[contains(.,'每件取样:')]"
sample_Z = "//td[contains(.,'不需取样')]"
sample_yes = "//button[@class='mr-4 my-1 v-btn v-btn--contained theme--light v-size--default primary']"

