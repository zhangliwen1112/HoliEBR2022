# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 14:27 
# @Author : 张丽雯 
# @File : MIreviewPage.py 
# @中文描述 :  批记录复核页面元素 --demo10 MI执行完成

# 登录页码元素
manufacture = "//*[contains(text(),'生产管理')]"
MIreview = "//*[contains(text(),'批记录复核')]"

# MI执行上端按钮
open = "//span[text()='打开']"
current = "//span[text()='当前']"
all = "//span[text()='全部']"
record = "//span[text()='批记录']"
refresh = "//span[text()='刷新']"

#筛选
select = "//span[text()='筛选']"
select_lot = "//span[@ref='eTitle'][text()='批次号']"
select1_text1 = "//input[@ref='eInput' and @placeholder='过滤条件...']"

# ----------------------------打开页面的元素------------------------------
approve = "//span[text()='批准']"
reject = "//span[text()='驳回']"
re_review = "//span[text()='重新复核']"
close_wo = "//span[text()='关闭工单']"
record1 = "//div[@class='v-card__text']//span[text()='批记录']"
alter = "//span[text()='警示']"

# 批准 单签名
# 驳回 单签名
# 添加说明
add_detail_button = "//span[contains(.,'添加说明')]"
# 复核说明、添加说明
detail = "//textarea"
re_submit = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[text()='确定']"



