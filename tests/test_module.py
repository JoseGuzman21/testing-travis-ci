#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mymodule

class TestMyModule(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(mymodule.sum(10, 20), 30)

    def test_sum1(self):
        self.assertEqual(mymodule.sum(0, 0), 0)

    def test_sum2(self):
        self.assertEqual(mymodule.sum(-1, 5), 4)

    def test_sum3(self):
        self.assertEqual(mymodule.sum(-1, -4), -5)

    def test_sum4(self):
        self.assertEqual(mymodule.sum(10, 20), 30)
#if __name__ == "__main__":
#    unittest.main()