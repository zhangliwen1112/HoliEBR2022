#coding=gbk
from  ElementApp.LoginPage import *
from src.public.FunctionSet import *
from src.public.common.LoginData import *

# app登陆
def app_login(app_username, app_password):
    if (driver != None):
        new_maximize_window()
        new_get(appurl)
        new_type(username_input,app_username)
        new_type(password_input, app_password)
        new_click(selectws)
        sleep(2)
        new_click(firstws)
        sleep(2)
        new_click(wsyes)

        new_click(login_button)

        sleep(3)
        # if is_element_present(login_button):
        #     log.info("登录成功")
        #     return True
        # else:
        #     log.info("登录失败")
        #     sys.exit()

# app退出
def app_logout():
    new_click(logout)
    sleep(2)
    new_click(logout_button)
    # if is_element_present(username_input):
    #     log.info("退出登录成功")
    #     return True
    # else:
    #     log.info("退出登录失败")
    #     return False

# admin登陆
def admin_login(admin_username, admin_password):
    if (driver != None):
        new_maximize_window()
        new_get(adminurl)
        sleep(2)
        new_type(admin_username_input,admin_username)
        new_type(admin_password_input, admin_password)
        new_click(admin_login_button)
        sleep(3)

# admin退出
def admin_logout():
    new_click(adminlogout)
    sleep(2)
    new_click(admin_logout_button)
