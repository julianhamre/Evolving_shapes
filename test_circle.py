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
        self.c = cl.circle(1, 2, 2)
    
    def test_move(self):
        self.c.move(3)
        self.assertEqual(self.c.x, 8)

if __name__ == "__main__":
    unittest.main()
