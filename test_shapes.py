#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:36:48 2022

@author: julianhamre
"""

import unittest
import shapes as sh

class test_circle(unittest.TestCase):
    
    def setUp(self):
        self.c = sh.circle(1, 3.6, 5)

    def test_move(self):
        easy_c = sh.circle(1, 0, 0)
        easy_c.move(45, 1)
        self.assertAlmostEqual(easy_c.get_position()[0], 2**(1/2), 2)
        self.assertAlmostEqual(easy_c.get_position()[1], 2**(1/2), 2)
 
    def test_move_float_parameter(self):
        self.c.move(61.2, 11)
        self.assertAlmostEqual(self.c.get_position()[0], 14.1986, 2)
        self.assertAlmostEqual(self.c.get_position()[1], 24.2787, 2)

    def test_move_large_angle(self):
        c = sh.circle(1, -1, -2)
        c.move(120, 3)
        self.assertAlmostEqual(c.get_position()[0], -4)
        self.assertAlmostEqual(c.get_position()[1], 3.1962, 4)

    def interval_benchmark(self):
        benchmark = []
        [benchmark.append((2**(1/2)) * i) for i in range(1, 6)]
        return benchmark


class test_border(unittest.TestCase):
    
    def setUp(self):
        self.b = sh.border(3.2, 4, -5.4)
    
    def test_get_corners(self):
        benchmark_x = [4, 7.2, 7.2, 4, 4]
        benchmark_y = [-5.4, -5.4, -2.2, -2.2, -5.4]
        bnchs = [benchmark_x, benchmark_y]
        for i in range(2):
            self.assertEqual(self.b.get_corners()[i], bnchs[i]) 


class test_interaction(unittest.TestCase):
    
    def test_circle_with_border(self):
        b = sh.border(10, 3.5, 4)
        itr = sh.interaction()
        
        circles_outside = [sh.circle(1, 14.6, 7), sh.circle(2.1, 30, 15), sh.circle(1, 6, -2)]
        hits = [[90], [90, 0], [0]]
        
        for i in range(len(circles_outside)):
            self.assertEqual(itr.circle_with_border(circles_outside[i], b), hits[i])
        
        circles_inside = [sh.circle(1, 4.6, 5.1), sh.circle(2, 11.4, 11.9)]
        
        for i in range(len(circles_inside)):
            self.assertEqual(itr.circle_with_border(circles_inside[i], b), [])


class test_manager(unittest.TestCase):
    
    def test_emit(self):
        c = sh.circle(0.5, 9, 5)
        b = sh.border(15, 2, 2)
        m = sh.manager(c, b)
        m.set_time_interval(0.1)
        m.set_show_plot(True)
        m.emit(28, 40)
        
        circle_position = [c.get_position()[0], c.get_position()[1]]
        benchmark_position = [10.059537111430785, 14.389431255717867]
        
        for i in range(len(circle_position)):
            self.assertAlmostEqual(circle_position[i], benchmark_position[i], 1)


if __name__ == "__main__":
    unittest.main()
