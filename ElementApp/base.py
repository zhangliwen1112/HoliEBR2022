from selenium.webdriver.common.action_chains import ActionChains


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def f5(self):
        return self.driver.refresh()

    def maxmize_window(self):
        return self.driver.maximize_window()

    def move_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def clear_text(self, element):
        element.clear()

    def click(self, element):
        element.click()

    def input_text(self, element, value):
        element.send_keys(value)

