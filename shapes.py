#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np


class aggressivity_color:
    
    def __init__(self, aggressivity_value):
        self.__aggressivity = aggressivity_value
    
    def __RGB(self):
        if self.__aggressivity > 0:
            rgb = [255, 255 - self.__aggressivity * 255, 0]
        else:
            rgb = [255 + self.__aggressivity * 255, 255, 0]
        
        return rgb
    
    def RGB_float(self):
        rgb_float = []
        for value in self.__RGB():
            rgb_float.append(value / 255)
        
        return rgb_float
    

class circle():
    _speed = 2
    _angle = 45
    _r_angle = np.radians(_angle)
    _aggressivity = 0
    # add scheduled pattern
    
    def __init__(self, radius, x_coordinate, y_coordinate):
        self._radius = radius
        self._x = x_coordinate
        self._y = y_coordinate
        self.__set_color()
    
    def get_color(self):
        return self.__color
    
    def __set_color(self):
        color = aggressivity_color(self._aggressivity)
        self.__color = color.RGB_float()
        
    def get_aggressivity(self):
        return self._aggressivity
    
    def __check_aggressivity_validity(self):
        if self._aggressivity > 1 or self._aggressivity < -1:
            raise ValueError("aggressivity value must be between -1 and 1")
    
    def set_aggressivity(self, aggressivity):
        self._aggressivity = aggressivity
        self.__check_aggressivity_validity()
        self.__set_color()
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius
    
    def area(self):
        return np.pi*self._radius**2
    
    def add_area(self, area):
        new_area = self.area() + area
        new_radius = (new_area / np.pi)**(1/2)
        self.set_radius(new_radius)
    
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

