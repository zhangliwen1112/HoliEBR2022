#coding=utf-8

"""
Created on 2020/11/16
@author: lianxiujuan
@desc: 标签管理
"""


# 登录页码元素
labelmg = "//div[text()='标签管理']"

# 标签组
area = "//div[@class='flex sm3']//div[contains(text(),'区域')]"
sector = "//div[@class='flex sm3']//div[contains(text(),'区段')]"
location = "//div[@class='flex sm3']//div[contains(text(),'位置')]"
reservior = "//div[@class='flex sm3']//div[contains(text(),'库区')]"
storagelocation = "//div[@class='flex sm3']//div[contains(text(),'库位')]"
container = "//div[@class='flex sm3']//div[contains(text(),'容器')]"
MIcontainer = "//div[@class='flex sm3']//div[contains(text(),'MI产出容器')]"
ocontainer = "//div[@class='flex sm3']//div[contains(text(),' 产出容器')]"
rcontainer = "//div[@class='flex sm3']//div[contains(text(),' 接收容器')]"
precontainer = "//div[@class='flex sm3']//div[contains(text(),'预产出容器')] "
pallet = "//div[@class='flex sm3']//div[contains(text(),'托盘')]"
opallet = "//div[@class='flex sm3']//div[contains(text(),'产出托盘')]"
rpallet = "//div[@class='flex sm3']//div[contains(text(),'接收托盘')]"
weigh = "//div[@class='flex sm3']//div[contains(text(),'称量')]"
weighpallet = "//div[@class='flex sm3']//div[contains(text(),'称量托盘')]"
device = "//div[@class='flex sm3']//div[contains(text(),'设备')]"

# 各标签组下新增/编辑/删除/设置默认模板
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
delete = "//span[text()='删除']"
setdefault = "//span[text()='设置默认模板']"

# 新增/编辑界面元素
allinput = "//div[@class='layout row wrap']//input[@type='text']"
zpl = '//textarea'
yes_button = "//span[contains(.,'确定')]"
cancel_button = "//span[contains(.,'取消')]"

delete_yes_button = "//button[@color='red']//span[contains(text(),'确定')]"

searchresult = '//div[@row-index="0"]//div[@aria-colindex="3"]'
