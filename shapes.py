#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np


class circle:
    __speed = 2
    # add default angle as 0
    
    def __init__(self, radius, x_coordinate, y_coordinate):
        self.__radius = radius
        self.__x = x_coordinate
        self.__y = y_coordinate
    
    def get_radius(self):
        return self.__radius
    
    def get_position(self):
        return [self.__x, self.__y]
    
    def set_angle(self, angle):
        self.__angle = angle
        
    def get_angle(self):
        return self.__angle
    
    def move(self, direction_angle, time):  # set direction angle to the circles angle attribute
        distance = self.__speed * time
        radians_angle = np.radians(direction_angle)  
        self.__x += np.cos(radians_angle) * distance
        self.__y += np.sin(radians_angle) * distance

    def get_points(self):
        angles = np.linspace(0, 2*np.pi, 100)
        x = []
        y = []
        for angle in angles:
            x.append(self.__radius * np.cos(angle) + self.__x)
            y.append(self.__radius * np.sin(angle) + self.__y)
        return [x, y]


class border:
    
    def __init__(self, side_length, x_coordinate, y_coordinate):
        self.__side = side_length
        
        # coordinates for bottom left corner
        self.__x = x_coordinate
        self.__y = y_coordinate
   
    def get_side(self):
        return self.__side
    
    def get_position(self):
        return [self.__x, self.__y]

    def get_corners(self):
        x = self.__x
        sx = x + self.__side
        y = self.__y
        sy = y + self.__side
        
        x = [x, sx, sx, x, x]
        y = [y, y, sy, sy, y]

        return [x, y]

