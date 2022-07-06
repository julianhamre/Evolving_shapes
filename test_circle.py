#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:36:48 2022

@author: julianhamre
"""

import unittest
import circle as cl

class test_circle(unittest.TestCase):
    
    def setUp(self):
        self.c = cl.circle(1, 3.6, 5)

    def test_move(self):
        easy_c = cl.circle(1, 0, 0)
        easy_c.move(45, 1)
        self.assertAlmostEqual(easy_c.x, 2**(1/2), 2)
        self.assertAlmostEqual(easy_c.y, 2**(1/2), 2)
 
    def test_move_float_parameter(self):
        self.c.move(61.2, 11)
        self.assertAlmostEqual(self.c.x, 14.1986, 2)
        self.assertAlmostEqual(self.c.y, 24.2787, 2)

    def test_move_large_angle(self):
        c = cl.circle(1, -1, -2)
        c.move(120, 3)
        self.assertAlmostEqual(c.x, -4)
        self.assertAlmostEqual(c.y, 3.1962, 4)

    def interval_benchmark(self):
        benchmark = []
        [benchmark.append((2**(1/2)) * i) for i in range(1, 6)]
        return benchmark

    def test_move_in_intervals(self):
        c = cl.circle(1, 0, 0)
        positions = c.move_in_intervals(45, 4, 5)
        for i in range(2):
            pts = positions[i]
            for j in range(len(pts)):
                self.assertAlmostEqual(pts[j], self.interval_benchmark()[j], 10) 
        

class test_border(unittest.TestCase):
    
    def setUp(self):
        self.b = cl.border(3.2, 4, -5.4)
    
    def test_get_corners(self):
        benchmark_x = [4, 7.2, 7.2, 4, 4]
        benchmark_y = [-5.4, -5.4, -2.2, -2.2, -5.4]
        bnchs = [benchmark_x, benchmark_y]
        for i in range(2):
            self.assertEqual(self.b.get_corners()[i], bnchs[i]) 


if __name__ == "__main__":
    unittest.main()
