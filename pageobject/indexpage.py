# -*- encoding:utf-8 -*-
from pageobject import PageObject
from urls import INDEX_PAGE_URL

class IndexPage(PageObject):
    url=INDEX_PAGE_URL
    page_flag_keyword = u'ovc1024'
    page_flag_xpath = '//img[@title="ovc1024"]'