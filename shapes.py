#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np


class circle():
    _color = "steelblue"
    _speed = 2
    _angle = 45
    _r_angle = np.radians(_angle)
    
    def __init__(self, radius, x_coordinate, y_coordinate):
        self._radius = radius
        self._x = x_coordinate
        self._y = y_coordinate
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    def get_radius(self):
        return self._radius
    
    def get_position(self):
        return [self._x, self._y]
    
    def set_angle(self, angle):
        self._angle = angle
        self._r_angle = np.radians(angle)
        
    def get_angle(self):
        return self._angle
    
    def get_x_speed(self):
        return np.cos(self._r_angle) * self._speed
    
    def get_y_speed(self):
        return np.sin(self._r_angle) * self._speed
    
    def move(self, time): 
        distance = self._speed * time
        self._x += np.cos(self._r_angle) * distance
        self._y += np.sin(self._r_angle) * distance

    def get_points(self):
        angles = np.linspace(0, 2*np.pi, 100)
        x = []
        y = []
        for angle in angles:
            x.append(self._radius * np.cos(angle) + self._x)
            y.append(self._radius * np.sin(angle) + self._y)
        return [x, y]


class aggresive_circle(circle):
    
    def __init__(self, radius, x_coordinate, y_coordinate):
        super().__init__(radius, x_coordinate, y_coordinate)
        self._init_agg_circ_()
            
        
    def _init_agg_circ_(self):
        self._color = "red"
        self._radius += 0

    

def transform_circle(circle, new_circle_class):
    circle.__class__ = new_circle_class
    circle._init_agg_circ_()
    return circle
    


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

