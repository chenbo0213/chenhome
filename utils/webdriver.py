# -*- encoding:utf-8 -*-
from utils.log import debug
from utils.abs import Singleton
from congig import DRIVER
from selenium import webdriver


@Singleton
class WebDriver():
    driver=None

    def __init__(self):
        if self.driver==None:
            debug('webdriver ->初始化driver：%s'%DRIVER)
            if DRIVER=='Chrome':
                self.driver=webdriver.Chrome()
            else:
                self.driver=webdriver.Firefox()
        else:
            debug('webdriver ->%s driver已经实例化。'%DRIVER)

    def get_driver(self):
        debug('webdriver  ->获取并返回当前driver实例。')
        return self.driver
driver=WebDriver().get_driver()
debug('webdriver.py  -> 实例化并返回当前driver实例：%s'%str(driver))