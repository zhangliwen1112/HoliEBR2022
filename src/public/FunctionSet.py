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


# 解析定位的元素，返回locator
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


# 隐式等待
def new_implicitly_wait(p_time):
    driver.implicitly_wait(10)


#  进入浏览器
def new_get(url):
    driver.get(url)
    print(threading.currentThread().name)
    print(threading.currentThread().ident)


# 放大浏览器
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


# 单击全选删除 输入
def new_type(p_object, p_value):
    # 点击
    ele = new_click(p_object)
    # 全选
    ele.send_keys(Keys.CONTROL, 'a')
    # 删除
    ele.send_keys(Keys.DELETE)
    ele.send_keys(p_value)


def new_type_ele(ele, p_value):
    # 全选
    new_click_ele(ele)
    ele.send_keys(Keys.CONTROL, 'a')
    # 删除
    ele.send_keys(Keys.DELETE)
    ele.send_keys(p_value)


# 双击全选删除 输入
def new_type_double(p_object, p_value):
    # 双击全选
    new_double_click(p_object)
    sleep(1)
    # 输入
    new_find_element(p_object).send_keys(p_value)



# 双击全选删除 输入
def new_type_double_ele(ele, p_value):
    # 双击全选
    new_double_click_ele(ele)
    sleep(1)
    # 输入
    ele.send_keys(p_value)


# 判断页面元素不可见
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


# 通过js点击
def new_click1(p_object):
    new_execute_script("arguments[0].click()", p_object)


# 通过js获取元素值，元素为xpath
def new_js_text(p_object):
    js = "return document.evaluate('"+p_object+"', document).iterateNext().value"
    return driver.execute_script(js)





# 移动到元素顶部
def new_scroll_to_element(p_object):
    new_execute_script("arguments[0].scrollIntoView(true);", p_object)


# 滚动条移动到顶部
def new_scroll_to_top():
    new_execute_script("var q=document.documentElement.scrollTop=0")
    # 滚动条移动到顶部


def new_scroll_to_button():
    # 滚动条移动到底部
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


# 获取文本
def new_get_text(p_object):
    element = new_find_element(p_object)
    textcontent = element.text
    return textcontent


# 获取文本
def new_get_text_ele(ele):
    textcontent = ele.text
    return textcontent


# 清空内容
def new_clear(p_object):
    # 点击new_clear
    ele = new_click(p_object)
    # 全选
    ele.send_keys(Keys.CONTROL, 'a')
    # 删除
    ele.send_keys(Keys.DELETE)


# 回退
def new_backspace(p_object):
    ele = new_click(p_object)
    # 回退一个字符
    ele.send_keys(Keys.BACK_SPACE)


# 向前一页
def new_back():
    driver.back()


# 后退一页
def new_forward():
    driver.forward()


# 退出浏览器
def new_quit():
    driver.quit()


# 刷新页面
def new_refresh():
    driver.refresh()


# 判断页面元素是否存在
def new_page_source(text):
    if text in driver.page_source:
        return True
    else:
        return False


# ==================================================鼠标键盘操作===========================================================
# 鼠标右击
def new_context_click(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.context_click(element).perform()


# 鼠标双击
def new_double_click(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.double_click(element).perform()


# 鼠标双击
def new_double_click_ele(ele):
    action = ActionChains(driver)
    action.double_click(ele).perform()


# 鼠标左键不松开
def new_click_and_hold(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.click_and_hold(element).perform()


# 元素拖拽到目标元素
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


# 鼠标移动到目标元素
def new_move_to_element(p_object):
    action = ActionChains(driver)
    element = new_find_element(p_object)
    action.move_to_element(element).perform()


# Control+组合快捷键
def xx():
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()


# 上传文件、图片。upload：上传文件需要的exe，file：上传文件的文件（如：hollysys.png）
def new_upload(upload, file):
    # 获取当前执行文件的目录
    file_dir = os.getcwd()
    # 获取项目存在的磁盘
    base_root = file_dir.split("\\HollEBR-UI")[0]
    # 拼接存在文件的目录
    material_path = base_root + "\\HoliEBR-UI\\src\\public\\upload\\"
    # 上传文件可执行文件exe的路径
    upload = material_path + upload
    # 上传文件的路径
    file = material_path + file
    # 把可执行文件的路径和上传文件的路径拼接成一个字符串
    uploadfile = upload + " " + file
    # 上传文件
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


# 滑动滚动条到当前窗口底部
def new_move(p_object):
    ele = new_find_element(p_object)
    # 等待元素可见
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(ele))
    # 将滚动条下拉至最低
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
