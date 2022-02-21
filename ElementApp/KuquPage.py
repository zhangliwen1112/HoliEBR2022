# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 14:18 
# @Author : 张丽雯 
# @File : kuquPage.py 
# @中文描述 :  库区管理
# 登录页码元素
inventory = "//*[contains(text(),'库存管理')]"
reservoir = "//*[contains(text(),'库区')]"


# 砝码配置上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
delete = "//span[contains(.,'删除')]"
refresh = "//span[contains(.,'刷新')]"
lable = "//span[contains(.,'标签')]"
diagram = "//span[contains(.,'图示')]"
relation = "//span[contains(.,'关联')]"

#新增、编辑页面元素
code = "//div[2]/div[2]/div/div/div[2]/form/div/div/div[1]/div/div/div[1]/div/input"
name = "//div[2]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input"
changqu = "//div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div[1]/div/div[1]/div[1]/input"
select_changqu1 = "//td/div/div"
select_submit = '//div[3]/div/div[3]/button/span'
quyu = '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[4]/div/div/div[1]/div[1]/div[1]'

select_quyu1 = "//body/div/div[4]/div/div/div"
location = '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[5]/div/div/div[1]/div[1]/div[1]'
add_location1 = '//body/div/div[5]/div/div/div[1]/div/div'
edit_location2 = '//div[@class="v-list-item__content"]'
submit = "//button//span[text()='确定']"
cancle = "//button[contains(.,'取消')]"


#删除确定、取消
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

#关联
relation_kuwei = '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[' \
                 '2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div '
relation_button = "//span[contains(.,'<')]"
remove_button = "//span[contains(.,'>')]"
remove_first = "//div[@class='flex d-flex xs5']//div[@role='gridcell']"
#选中第一条
first = '//div[@role="row" and @row-index="0"]'
