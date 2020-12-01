#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mymodule

class TestMyModule(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mymodule.sum(1, 2), 3)

    def test_sum1(self):
        self.assertEqual(mymodule.sum(10, 20), 30)

    def test_sum2(self):
        self.assertEqual(mymodule.sum(100, 200), 300)

    def test_sum3(self):
        self.assertEqual(mymodule.sum(500, 700), 1200)

    def test_sum4(self):
        self.assertEqual(mymodule.sum(1000, 2000), 3000)

    def test_sum5(self):
        self.assertEqual(mymodule.sum(120020, 80), 120100)

    def test_sum6(self):
        self.assertEqual(mymodule.sum(1200000, 1200000), 2400000)

    def test_sum7(self):
        self.assertEqual(mymodule.sum(120000000, 120000000), 240000000)

if __name__ == "__main__":
    unittest.main()