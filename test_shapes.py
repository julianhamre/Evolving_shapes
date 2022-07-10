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
        self.assertAlmostEqual(easy_c.x, 2**(1/2), 2)
        self.assertAlmostEqual(easy_c.y, 2**(1/2), 2)
 
    def test_move_float_parameter(self):
        self.c.move(61.2, 11)
        self.assertAlmostEqual(self.c.x, 14.1986, 2)
        self.assertAlmostEqual(self.c.y, 24.2787, 2)

    def test_move_large_angle(self):
        c = sh.circle(1, -1, -2)
        c.move(120, 3)
        self.assertAlmostEqual(c.x, -4)
        self.assertAlmostEqual(c.y, 3.1962, 4)

    def interval_benchmark(self):
        benchmark = []
        [benchmark.append((2**(1/2)) * i) for i in range(1, 6)]
        return benchmark

    def test_move_in_intervals(self):
        c = sh.circle(1, 0, 0)
        positions = c.move_in_intervals(45, 4, 5)
        for i in range(2):
            pts = positions[i]
            for j in range(len(pts)):
                self.assertAlmostEqual(pts[j], self.interval_benchmark()[j], 10) 
        

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
        
        

class test_optional(unittest.TestCase):

    def test_set_value(self):
        op = sh.optional(True)
        with self.assertRaises(AttributeError):
            op.value
        op.set_value(90)
        try:
            op.value
        except AttributeError:
            self.fail("AttributeError raised after value attribute should have been set")


class test_manager(unittest.TestCase):
    
    def test_emit(self):
        c = sh.circle(0.5, 9, 5)
        b = sh.border(15, 2, 2)
        m = sh.manager(c, b)
        m.set_time_interval(0.1)
        m.emit(28, 40)
        
        circle_position = [c.x, c.y]
        benchmark_position = [10.059537111430785, 14.389431255717867]
        
        for i in range(len(circle_position)):
            self.assertAlmostEqual(circle_position[i], benchmark_position[i], 1)


if __name__ == "__main__":
    unittest.main()
