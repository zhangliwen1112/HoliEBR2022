#coding=utf-8

from ElementAdmin.base import Page
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
"""
登录页面对象定义
"""

class Login(Page):
    # 定位器
    username = (By.CSS_SELECTOR, "input[placeholder='请输入用户名']")
    password = (By.CSS_SELECTOR, "input[placeholder='请输入密码']")
    login_button = (By.XPATH, '//*[contains(text(),"登 录")]')

    # 输入用户名
    def username_input(self, text):
        return self.find_element(*self.username).send_keys(text)

    # 输入密码
    def password_input(self, text):
        return self.find_element(*self.password).send_keys(text)

    # 点击登录
    def login_click(self):
        return self.find_element(*self.login_button).click()

    # 登录方法
    def login_action(self, username, password):
        self.username_input(username)
        self.password_input(password)
        time.sleep(10)
        self.login_click()
        time.sleep(6)