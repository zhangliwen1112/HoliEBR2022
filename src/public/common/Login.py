#coding=gbk
from  ElementApp.LoginPage import *
from src.public.FunctionSet import *
from src.public.common.LoginData import *

# app��½
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
        #     log.info("��¼�ɹ�")
        #     return True
        # else:
        #     log.info("��¼ʧ��")
        #     sys.exit()

# app�˳�
def app_logout():
    new_click(logout)
    sleep(2)
    new_click(logout_button)
    # if is_element_present(username_input):
    #     log.info("�˳���¼�ɹ�")
    #     return True
    # else:
    #     log.info("�˳���¼ʧ��")
    #     return False

# admin��½
def admin_login(admin_username, admin_password):
    if (driver != None):
        new_maximize_window()
        new_get(adminurl)
        sleep(2)
        new_type(admin_username_input,admin_username)
        new_type(admin_password_input, admin_password)
        new_click(admin_login_button)
        sleep(3)

# admin�˳�
def admin_logout():
    new_click(adminlogout)
    sleep(2)
    new_click(admin_logout_button)
