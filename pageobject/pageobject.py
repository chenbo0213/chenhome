# -*- encoding:utf-8 -*-
from utils.log import debug
from utils.webdriver import driver

class PageObject():
    url=None
    page_flag_xpath=None
    page_flag_keyword=None

    def __init__(self):
        self.driver=driver
        debug('pageobject  -> %s获取当前driver的实例'%self.driver)

    def open_and_check(self):
        debug('pageobject  ->打开并检测指定url页面。')
        self.driver.get(self.url)
        return self.check_if_page_opened()

    def check_if_page_opened(self):
        flag_element=self.driver.find_element_by_xpath(self.page_flag_xpath)
        if self.page_flag_keyword==flag_element:
            return True
        else:
            return False