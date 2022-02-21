#coding=utf-8

"""
Created on 2020/9/14
@author: lianxiujuan
@desc: MI执行--重复称量
"""


manufacture = "//*[contains(text(),'生产管理')]"
miexct = "//*[contains(text(),'MI执行')]"

# MI执行上端按钮
wo = "//div[@id='mi-excute-layout']/div/div/div/div/div/div/input"
wo1 = "//td/div/div"
woyes = "//div[3]/div/div[3]/button/span"
containerlist = "//span[contains(.,'容器列表')]"
container1 = "//div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]"
yes = "//span[contains(.,'确定')]"
verify = "//span[contains(.,'验证')]"
value = "//form/div[3]/div[2]/div/div/div/div/div/div/input"
no = "//span[contains(.,'否')]"
