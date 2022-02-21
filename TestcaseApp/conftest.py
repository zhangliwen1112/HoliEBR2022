# -*- coding: utf-8 -*- 
# @Time : 2021/1/14 17:43 
# @Author : 张丽雯 
# @File : conftest.py 
# @中文描述 :  当测试失败的时候，自动截图，展示到html报告中

# conftest.py文件
# coding:utf-8
import os

from selenium import webdriver
import pytest
from src.public.WebDriverLib import WebDriverLib
from src.public.common.Login import app_login, app_logout

wb = WebDriverLib()

driver = wb.driver
log = wb.logger


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            base_dir = os.getcwd()
            base = base_dir.split("\\HoliEBR-UI\\")[0]
            dirpng = base + "\\HoliEBR-UI\\report\\image\\"
            if os.path.exists(dirpng) and os.path.isdir(dirpng):
                pass
            else:
                os.mkdir(dirpng)
            file_name = dirpng + report.nodeid.replace("::", "_") + ".png"
            file_name1 = '\\HoliEBR-UI\\report\\image\\' + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name1
                # extra.append(pytest_html.extras.html(html))


def _capture_screenshot(name):
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    driver.get_screenshot_as_file(name)
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver


def pytest_collection_modifyitems(session, items):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


# 前后置预置条件
@pytest.fixture(scope='session', autouse=True)
def app_setup_function():
    username = 'wang'
    password = '1'
    app_login(username, password)
    yield  # 后置
    app_logout()
    driver.quit()
