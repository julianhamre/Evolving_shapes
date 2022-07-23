#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 19:00:09 2022

@author: julianhamre
"""

import unittest
import interaction
import shapes as sh


class test_border_interaction(unittest.TestCase):
    
    def test_hits(self):
        b = sh.border(10, 3.5, 4)
        
        circles_outside = [sh.circle(1, 14.6, 7), sh.circle(2.1, 30, 15), sh.circle(1, 6, -2)]
        hits = [[90], [90, 0], [0]]
        
        for i in range(len(circles_outside)):
            itr = interaction.border(b, circles_outside[i])
            self.assertEqual(itr.hits(), hits[i])
        
        circles_inside = [sh.circle(1, 4.6, 5.1), sh.circle(2, 11.4, 11.9)]
        
        for i in range(len(circles_inside)):
            itr = interaction.border(b, circles_inside[i])
            self.assertEqual(itr.hits(), [])


class test_circle_interaction(unittest.TestCase):  
      
    def test_overlap(self):
        circles = [sh.circle(1, 2, 2), sh.circle(2, 5, 7), sh.circle(1, 15, 7.5)]
        overlapping = [sh.circle(1, 3, 2), sh.circle(2, 5, 10.9), sh.circle(0.5, 16, 8.5)]
        not_overlapping = [sh.circle(1, 10, 2), sh.circle(2, 5, 15), sh.circle(1, 17, 9.5)]
        
        for i in range(len(circles)):
            itr = interaction.circle(circles[i], overlapping[i])
            self.assertTrue(itr.overlap())
            not_itr = interaction.circle(circles[i], not_overlapping[i])
            self.assertFalse(not_itr.overlap())


if __name__ == "__main__":
    unittest.main()