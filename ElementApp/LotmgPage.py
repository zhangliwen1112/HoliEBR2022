#coding=utf-8

"""
Created on 2021/1/7
@author: lianxiujuan
@desc: 批次管理
"""


lotmg = "//div[@class='v-list-item theme--light']//*[text()='批次管理']"
lotmg_lotmg = "//div[2]/div/div/a[2]/div[text()='批次管理']"

# 批次管理上端按钮
maintenance = "//*[text()='批次维护']"
locklot = "//*[text()='锁定批次']"
rejectlot = "//*[text()='驳回批次']"
lockcon = "//*[text()='锁定容器']"
rejectcon = "//*[text()='驳回容器']"

# 批次维护
resample = "//span[text()='重取样']"
sample = "//span[text()='取样']"
analysis_density_potency = "//div[2]/div/div/div[4]/div/div/div/div/div/input"
select = "//div[@class='v-card v-sheet theme--light']//i[text()='arrow_drop_down']"
phavalue = "//div[text()='中国药典']"
statusvalue = "//div[@role='listbox']//div[text()='带条件批准']"
yes = "//div[@class='v-card v-sheet theme--light']//span[text()='确定']"

yes_primary = '//button[@color="primary"]'

# 锁定容器、驳回容器
containerid = '//form/div/div/div/div/div/div/input'
