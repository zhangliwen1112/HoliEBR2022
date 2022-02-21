import os
import threading

import time
# import win32api
# import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.public.CommonLib import CommonLib
from src.public.WebDriverLib import WebDriverLib

wb = WebDriverLib()

driver = wb.driver
log = wb.logger


def new_teardown():
    driver.quit()


# ������λ��Ԫ�أ�����locator
def paseobject(p_object):
    if (p_object.startswith("./") or p_object.startswith("//")):
        return (By.XPATH, p_object)
    elif (p_object.startswith("link") or p_object.startswith("Link")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.LINK_TEXT, newObjecyt)
    elif (p_object.startswith("plink") or p_object.startswith("pLink")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.PARTIAL_LINK_TEXT, newObjecyt)
    elif (p_object.startswith("xpath")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.XPATH, newObjecyt)
    elif (p_object.startswith("id")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.ID, newObjecyt)
    elif (p_object.startswith("css")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.CSS_SELECTOR, newObjecyt)
    elif (p_object.startswith("class")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return {"by": By.CLASS_NAME, "value": newObjecyt}
    elif (p_object.startswith("tagName")):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.TAG_NAME, newObjecyt)
    elif (p_object.startswith('name')):
        newObjecyt = p_object[p_object.find("=") + 1:].strip()
        return (By.NAME, newObjecyt)
    else:
        return None


# ��ʽ�ȴ�
def new_implicitly_wait(p_time):
    driver.implicitly_wait(10)


#  ���������
def new_get(url):
    driver.get(url)
    print(threading.currentThread().name)
    print(threading.currentThread().ident)


# �Ŵ������
def new_maximize_window():
    driver.maximize_window()


def new_find_element(p_object):
    count = 0
    while True:
        count += 1
        try:
            p_obj = paseobject(p_object)
            w_ele = driver.find_element(*p_obj)
            return w_ele
        except  Exception as  e:
            print(str(e) + "new_find_element")
            if count < 4:
                CommonLib.sleep(1)

                continue
            else:
                raise


def new_find_elements(p_object):
    count = 0
    while True:
        count += 1
        try:
            p_obj = paseobject(p_object)
            w_ele_list = driver.find_elements(*p_obj)
            if not w_ele_list and count < 5:
                CommonLib.sleep(1)
                continue
            return w_ele_list
        except  Exception as e:
            if count < 3:
                CommonLib.sleep(1)
                continue
            else:
                raise


def new_click(p_object):
    count = 0
    ele = new_find_element(p_object)
    while True:
        count += 1
        try:
            ele.click()
            return ele
        except  Exception as e:
            print(str(e) + "new_click")
            if count < 20:
                CommonLib.sleep(1)
                continue
            else:
                raise


def new_click_ele(web_ele):
    count = 0
    while True:
        try:
            web_ele.click()
            return
        except Exception as e:
            print(str(e) + "new_click_ele")
            if count < 20:
                count += 1
                CommonLib.sleep(1)
                continue
            else:
                raise


def new_send_keys(p_object, p_value):
    ele = new_find_element(p_object)
    ele.send_keys(p_value)


def new_send_keys_ele(web_ele, p_value):
    web_ele.send_keys(Keys.CONTROL, 'a')
    web_ele.send_keys(Keys.DELETE)
    web_ele.send_keys(p_value)


# ����ȫѡɾ�� ����
def new_type(p_object, p_value):
    # ���
    ele = new_click(p_object)
    # ȫѡ
    ele.send_keys(Keys.CONTROL, 'a')
    # ɾ��
    ele.send_keys(Keys.DELETE)
    ele.send_keys(p_value)


def new_type_ele(ele, p_value):
    # ȫѡ
    new_click_ele(ele)
    ele.send_keys(Keys.CONTROL, 'a')
    # ɾ��
    ele.send_keys(Keys.DELETE)
    ele.send_keys(p_value)


# ˫��ȫѡɾ�� ����
def new_type_double(p_object, p_value):
    # ˫��ȫѡ
    new_double_click(p_object)
    sleep(1)
    # ����
    new_find_element(p_object).send_keys(p_value)



# ˫��ȫѡɾ�� ����
def new_type_double_ele(ele, p_value):
    # ˫��ȫѡ
    new_double_click_ele(ele)
    sleep(1)
    # ����
    ele.send_keys(p_value)


# �ж�ҳ��Ԫ�ز��ɼ�
def is_element_invisable(p_object):
    try:
        WebDriverWait(driver, 3).until(EC.invisibility_of_element(paseobject(p_object)))
        return True
    except:
        return False


def is_element_present(p_object):
    try:

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(paseobject(p_object)))
        return True
    except:
        return False


def is_text_clickable(text):
    try:
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(paseobject(".//*[contains(text(),'" + text + "')]")))
        return True
    except:
        return False


def is_text_present(text):
    try:

        WebDriverWait(driver, 10).until(
            EC.visibility_of(new_find_element(".//*[contains(text(),'" + text + "')]")))
        return True
    except:
        return False


def is_element_clickable(p_object):
    try:

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(paseobject(p_object)))

        return True
    except:
        return False


def new_is_selected(p_object):
    attr = new_get_attribute(p_object, 'class')
    if attr.find('is-checked') > -1:
        return True
    else:
        return False


def new_execute_script(js, *p_object):
    if len(p_object) <= 0:
        return driver.execute_script(js)

    else:
        element = new_find_element(p_object[0])
        return driver.execute_script(js, element)


# ͨ��js���
def new_click1(p_object):
    new_execute_script("arguments[0].click()", p_object)


# ͨ��js��ȡԪ��ֵ��Ԫ��Ϊxpath
def new_js_text(p_object):
    js = "return document.evaluate('"+p_object+"', document).iterateNext().value"
    return driver.execute_script(js)





# �ƶ���Ԫ�ض���
def new_scroll_to_element(p_object):
    new_execute_script("arguments[0].scrollIntoView(true);", p_object)


# �������ƶ�������
def new_scroll_to_top():
    new_execute_script("var q=document.documentElement.scrollTop=0")
    # �������ƶ�������


def new_scroll_to_button():
    # �������ƶ����ײ�
    new_execute_script("document.documentElement.scrollTop?=?10000")


def new_get_current_url():
    current_url = driver.current_url()
    return current_url


def new_get_title():
    title = driver.title()
    return title


def new_get_attribute(p_object, name):
    element = new_find_element(p_object)
    attr = element.get_attribute(name)
    return attr


# ��ȡ�ı�
def new_get_text(p_object):
    element = new_find_element(p_object)
    textcontent = element.text
    return textcontent


# ��ȡ�ı�
def new_get_text_ele(ele):
    textcontent = ele.text
    return textcontent


# �������
def new_clear(p_object):
    # ���new_clear
    ele = new_click(p_object)
    # ȫѡ
    ele.send_keys(Keys.CONTROL, 'a')
    # ɾ��
    ele.send_keys(Keys.DELETE)


# ����
def new_backspace(p_object):
    ele = new_click(p_object)
    # ����һ���ַ�
    ele.send_keys(Keys.BACK_SPACE)


# ��ǰһҳ
def new_back():
    driver.back()


# ����һҳ
def new_forward():
    driver.forward()


# �˳������
def new_quit():
    driver.quit()


# ˢ��ҳ��
def new_refresh():
    driver.refresh()


# �ж�ҳ��Ԫ���Ƿ����
def new_page_source(text):
    if text in driver.page_source:
        return True
    else:
        return False


# ==================================================�����̲���===========================================================
# ����һ�
def new_context_click(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.context_click(element).perform()


# ���˫��
def new_double_click(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.double_click(element).perform()


# ���˫��
def new_double_click_ele(ele):
    action = ActionChains(driver)
    action.double_click(ele).perform()


# ���������ɿ�
def new_click_and_hold(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.click_and_hold(element).perform()


# Ԫ����ק��Ŀ��Ԫ��
def new_drag_and_drop(p_object, target):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    target_element = new_find_element(target)
    ActionChainsDriver = action.drag_and_drop(element, target_element)
    ActionChainsDriver.perform()


def new_drag_and_drop_by_offset(p_object, x, y):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    ActionChainsDriver = action.drag_and_drop_by_offset(element, xoffset=x, yoffset=y)
    ActionChainsDriver.perform()


# ����ƶ���Ŀ��Ԫ��
def new_move_to_element(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.move_to_element(element).perform()


# Control+��Ͽ�ݼ�
def xx():
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()


# �ϴ��ļ���ͼƬ��upload���ϴ��ļ���Ҫ��exe��file���ϴ��ļ����ļ����磺hollysys.png��
def new_upload(upload, file):
    # ��ȡ��ǰִ���ļ���Ŀ¼
    file_dir = os.getcwd()
    # ��ȡ��Ŀ���ڵĴ���
    base_root = file_dir.split("\\HollEBR-UI")[0]
    # ƴ�Ӵ����ļ���Ŀ¼
    material_path = base_root + "\\HoliEBR-UI\\src\\public\\upload\\"
    # �ϴ��ļ���ִ���ļ�exe��·��
    upload = material_path + upload
    # �ϴ��ļ���·��
    file = material_path + file
    # �ѿ�ִ���ļ���·�����ϴ��ļ���·��ƴ�ӳ�һ���ַ���
    uploadfile = upload + " " + file
    # �ϴ��ļ�
    os.system(uploadfile)
    driver.implicitly_wait(8)


# def new_win32api_drag_and_drop(src_x, src_y, mov_x, mov_y):
#     win32api.SetCursorPos((src_x, src_y))
#     CommonLib.sleep(1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, src_x, src_y)
#     CommonLib.sleep(1)
#     win32api.mouse_event(win32con.MOUSE_MOVED, mov_x, mov_y)
#     CommonLib.sleep(1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#     CommonLib.sleep(1)
#
#
# def new_win32api_mouse_click(x, y):
#     win32api.SetCursorPos((x, y))
#     CommonLib.sleep(1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
#     CommonLib.sleep(1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
#     CommonLib.sleep(1)


def sleep(p_time):
    time.sleep(p_time)


# ��������������ǰ���ڵײ�
def new_move(p_object):
    ele = new_find_element(p_object)
    # �ȴ�Ԫ�ؿɼ�
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(ele))
    # �����������������
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
