# -*- encoding:utf-8 -*-
import unittest
from pageobject.pageobject import PageObject

class MyTestCase(unittest.TestCase):
    def test_something(self):
        url='http://www.baidu.com'
        PageObject().open_and_check(url)



if __name__ == '__main__':
    unittest.main()
