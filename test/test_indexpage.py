# -*- encoding:utf-8 -*-
import unittest
from pageobject.indexpage import IndexPage

class MyTestCase(unittest.TestCase):
    def test_something(self):
       indexpage=IndexPage()
       indexpage.open_and_check()




if __name__ == '__main__':
    unittest.main()