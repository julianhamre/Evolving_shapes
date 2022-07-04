#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np

class circle:
    speed = 2
    
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
    
    def move(self, direction_angle, time):
        distance = self.speed * time
        radians_angle = np.radians(direction_angle)
        self.x += np.cos(radians_angle) * distance
        self.y += np.sin(radians_angle) * distance


