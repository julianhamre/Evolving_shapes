#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

class circle:
    speed = 2
    
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
    
    def move(self, time):
        self.x += self.speed * time


