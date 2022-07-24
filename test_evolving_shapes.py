#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 19:03:09 2022

@author: julianhamre
"""

import unittest
import evolving_shapes as ev
import shapes as sh

class test_manager(unittest.TestCase):
    
    def test_emit(self):
        c = sh.circle(0.5, 9, 5)
        c.set_angle(28)
        b = sh.border(15, 2, 2)
        m = ev.manager()
        m.set_border(b)
        m.set_time_interval(0.1)
        m.show_plot(False)
        m.emit([c], 40)
        
        circle_position = [c.get_position()[0], c.get_position()[1]]
        benchmark_position = [10.059537111430785, 14.389431255717867]
        
        for i in range(len(circle_position)):
            self.assertAlmostEqual(circle_position[i], benchmark_position[i], 1)
            

if __name__ == "__main__":
    unittest.main()
