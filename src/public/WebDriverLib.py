import operator
import os
import threading
import time


from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.public.CommonLib import CommonLib
from src.public.Logger import Log



class WebDriverLib:
    _instance_lock = threading.Lock()

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(WebDriverLib, "_instance"):
            with WebDriverLib._instance_lock:
                if not hasattr(WebDriverLib, "_instance"):
                    WebDriverLib._instance = object.__new__(cls)

                    # 创建Chrome浏览器配置对象实例
                    __chromeOptions = webdriver.ChromeOptions()
                    print(str(os.getcwd()).split(r'HoliEBR-111')[0] + "HoliEBR-111\\download")

                    # 如果该目录不存在，将会自动创建
                    __prefs = {"download.default_directory": str(os.getcwd()).split(r'HoliEBR-111')[0] + "HoliEBR-111\\download"}
                    # 将自定义设置添加到Chrome配置对象实例中
                    __chromeOptions.add_experimental_option("prefs", __prefs)
                    # 启动带有自定义设置的Chrome浏览器
                    WebDriverLib._instance.driver = webdriver.Chrome(options=__chromeOptions)

                    WebDriverLib._instance.logger = Log()
        return WebDriverLib._instance


    # def select_browser(self,name):
    #     self.logger = Logger(__name__)
    #     try:
    #         if name == "firefox" or name == "Firefox" or name == "ff":
    #             print("start browser name :Firefox")
    #             self.driver = webdriver.Firefox()
    #             return self.driver, self.logger
    #         elif name == "chrome" or name == "Chrome":
    #             print("start browser name :Chrome")
    #             self.driver = webdriver.Chrome()
    #             print(str(self.driver) + "sssssssssss")
    #             return self.driver, self.logger
    #         elif name == "ie" or name == "Ie":
    #             print("start browser name :Ie")
    #             self.driver = webdriver.Ie()
    #             return self.driver, self.logger
    #         elif name == "phantomjs" or name == "Phantomjs":
    #             print("start browser name :phantomjs")
    #             self.driver = webdriver.PhantomJS()
    #             return self.driver, self.logger
    #         else:
    #             print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘")
    #     except Exception as msg:
    #         print("启动浏览器出现异常：%s" % str(msg))
    #
    #     return self.driver, self.logger

    def new_teardown(self):
        self.driver.quit()

    # 解析定位的元素，返回locator
    def paseobject(self, p_object):
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
    def new_implicitly_wait(self, p_time):
        self.driver.implicitly_wait(10)

    #  进入浏览器
    def new_get(self, url):
        self.driver.get(url)

    # 放大浏览器
    def new_maximize_window(self):
        self.driver.maximize_window()

    def new_find_element(self, p_object):
        count = 0
        while True:
            count += 1
            try:
                p_obj = self.paseobject(p_object)
                w_ele = self.driver.find_element(*p_obj)
                return w_ele
            except  Exception as  e:
                print(e)
                if count < 4:
                    CommonLib.sleep(1)
                    print(Exception)
                    continue
                else:
                    raise
                    return

    def new_find_elements(self, p_object):
        count = 0
        while True:
            count += 1
            try:
                p_obj = self.paseobject(p_object)

                w_ele_list = self.driver.find_elements(*p_obj)
                if not w_ele_list and count < 3:
                    CommonLib.sleep(1)
                    continue
                return w_ele_list
            except  Exception as e:
                if count < 6:
                    CommonLib.sleep(1)
                    continue
                else:
                    raise
                    return
            #
            # p_obj = self.paseobject(p_object)
            # w_ele_list = self.driver.find_elements(*p_obj)
            # return w_ele_list


    def new_click(self, p_object):
        count = 0
        ele = self.new_find_element(p_object)
        while True:
            count += 1

            try:

                ele.click()
                return ele
            except  Exception:
                if count < 20:
                    CommonLib.sleep(1)
                    continue
                else:
                    raise
                    return

    def new_send_keys(self, p_object, p_value):
        ele = self.new_find_element(p_object)
        ele.send_keys(p_value)

    def new_type(self, p_object, p_value):
        # 点击
        ele = self.new_click(p_object)
        # 全选
        ele.send_keys(Keys.CONTROL, 'a')
        # 删除
        ele.send_keys(Keys.DELETE)
        ele.send_keys(p_value)



    # 判断页面元素不可见
    def is_element_invisable(self, p_object):
        try:
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element(self.paseobject(p_object)))
            return True
        except:
            return False

    def is_element_present(self, p_object):
        try:

            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.paseobject(p_object)))
            return True
        except:
            return False

    def is_text_clickable(self, text):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.paseobject(".//*[contains(text(),'" + text + "')]")))
            return True
        except:
            return False

    def is_text_present(self, text):
        try:

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of(self.new_find_element(".//*[contains(text(),'" + text + "')]")))
            return True
        except:
            return False

    def is_element_clickable(self, p_object):
        try:

            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.paseobject(p_object)))

            return True
        except:
            return False

    def new_is_selected(self, p_object):
        attr = self.new_get_attribute(p_object, 'class')
        if attr.find('is-checked') > -1:
            return True
        else:
            return False

    def new_execute_script(self, js, *p_object):
        if len(p_object) <= 0:
            return self.driver.execute_script(js)

        else:
            element = self.new_find_element(p_object[0])
            return self.driver.execute_script(js, element)

    # 利用js点击
    def new_click1(self, p_object):
        self.new_execute_script("arguments[0].click()", p_object)

    # 移动到元素顶部
    def new_scroll_to_element(self, p_object):
        self.new_execute_script("arguments[0].scrollIntoView(true);", p_object)

    # 滚动条移动到顶部
    def new_scroll_to_top(self):
        self.new_execute_script("document.documentElement.scrollTop?=?0")
        # 滚动条移动到顶部

    def new_scroll_to_button(self):
        # 滚动条移动到底部
        self.new_execute_script("document.documentElement.scrollTop?=?10000")

    def new_get_current_url(self):
        current_url = self.driver.current_url()
        return current_url

    def new_get_title(self):
        title = self.driver.title()
        return title

    def new_get_attribute(self, p_object, name):
        element = self.new_find_element(p_object)
        attr = element.get_attribute(name)
        return attr

    # 获取文本
    def new_get_text(self, p_object):
        element = self.new_find_element(p_object)
        textcontent = element.text
        return textcontent

    # 清空内容
    def new_clear(self, p_object):
        # 点击new_clear
        ele = self.new_click(p_object)
        # 全选
        ele.send_keys(Keys.CONTROL, 'a')
        # 删除
        ele.send_keys(Keys.DELETE)

    # 向前一页
    def new_back(self):
        self.driver.back()

    # 后退一页
    def new_forward(self):
        self.driver.forward()

    # 退出浏览器
    def new_quit(self):
        self.driver.quit()

    # 刷新页面
    def new_refresh(self):
        self.driver.refresh()

    # ==================================================鼠标键盘操作===========================================================
    # 鼠标右击
    def new_context_click(self, p_object):
        action = ActionChains(self.driver)
        element = self.new_find_element(p_object)
        action.context_click(element).perform()

    # 鼠标双击
    def new_double_click(self, p_object):
        action = ActionChains(self.driver)
        element = self.new_find_element(p_object)
        action.double_click(element).perform()

    # 拖拽--html5不支持
    def new_drag_and_drop(self, p_object, target):
        action = ActionChains(self.driver)
        element = self.new_find_element(p_object)
        target_element = self.new_find_element(target)
        action.drag_and_drop(element, target_element).perform()

    def new_drag_and_drop_by_offset(self, p_object,x,y):
        action = ActionChains(self.driver)
        element = self.new_find_element(p_object)
        action.drag_and_drop_by_offset(element, xoffset=x,yoffset=y).perform()
    # 鼠标移动到目标元素
    def new_move_to_element(self, p_object):
        action = ActionChains(self.driver)
        element = self.new_find_element(p_object)
        action.move_to_element(element).perform()


        # 上传文件、图片。upload：上传文件需要的exe，file：上传文件的文件（如：hollysys.png）

    def new_upload(self, upload, file):
        # 获取当前执行文件的目录
        file_dir = os.getcwd()
        # 获取项目存在的磁盘
        base_root = file_dir.split("\\Hollcube_UI")[0]
        # 拼接存在文件的目录
        material_path = base_root + "\\Hollcube_UI\\material\\"
        # 上传文件可执行文件exe的路径
        upload = material_path + upload
        # 上传文件的路径
        file = material_path + file
        # 把可执行文件的路径和上传文件的路径拼接成一个字符串
        uploadfile = upload + " " + file
        # 上传文件
        os.system(uploadfile)
        self.driver.implicitly_wait(8)

    # def new_win32api_drag_and_drop(self, src_x, src_y, mov_x, mov_y):
    #     win32api.SetCursorPos((src_x, src_y))
    #     CommonLib.sleep(1)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, src_x, src_y)
    #     CommonLib.sleep(1)
    #     win32api.mouse_event(win32con.MOUSE_MOVED, mov_x, mov_y)
    #     CommonLib.sleep(1)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    #     CommonLib.sleep(1)
    #
    # def new_win32api_mouse_click(self, x, y):
    #     win32api.SetCursorPos((x, y))
    #     CommonLib.sleep(1)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    #     CommonLib.sleep(1)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
    #     CommonLib.sleep(1)

