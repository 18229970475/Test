#!/usr/bin/python       
# -*- coding:UTF-8 -*-
import unittest

from HTMLTestRunner import HTMLTestRunner

from two import Count


class TestLogin(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_add(self):
        count = Count(2, 3)
        self.assertEqual(count.add(), 5)

    def test_add_one(self):
        count = Count(12, 30)
        self.assertEqual(count.add(), 41)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestLogin("test_add"))
    testsuite.addTest(TestLogin("test_add_one"))

    fp = open('./result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(testsuite)
    fp.close()