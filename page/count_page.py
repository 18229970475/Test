#!/usr/bin/python       
# -*- coding:UTF-8 -*-
import unittest

from entity.addSum import AddSum
from entity.subSum import SubSum


class CountTest(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_add(self):
        result = AddSum(2, 3)
        self.assertEqual(result.add_two(), 5)

    def  test_add_one(self):
        result = AddSum(4, 5)
        self.assertEqual(result.add_two(), 10)

    def test_sub(self):
        result = SubSum(7, 4)
        self.assertEqual(result.sub_sum(), 3)

    def test_sub_one(self):
        result = SubSum(8, 6)
        self.assertEqual(result.sub_sum(), 3)

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    '''
    suite = unittest.TestSuite()
    suite.addTest(CountTest("test_add"))
    suite.addTest(CountTest("test_add_one"))
    suite.addTest(CountTest("test_sub"))
    suite.addTest(CountTest("test_sub_one"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
     '''
    test_dir = "./"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='count*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)

