#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:02:00 2022

@author: julianhamre
"""

import numpy as np


class border_inter:

    def __init__(self, border, circle):
        self.__b = border
        self.__c = circle
    
    def hits(self):
        horizontal = 0
        vertical = 90
        hits = []
        
        cx = self.__c.get_position()[0]
        cy = self.__c.get_position()[1]
        cr = self.__c.get_radius()
        bx = self.__b.get_position()[0]
        by = self.__b.get_position()[1]
        bs = self.__b.get_side()
        
        if cx + cr >= bx + bs:
            hits.append(vertical)
        
        if cy + cr >= by + bs:
            hits.append(horizontal)
        
        if cx - cr <= bx:
            hits.append(vertical)
        
        if cy - cr <= by:
            hits.append(horizontal)
        
        return hits
    
    def outgoing_angle(self):
        hits = self.hits()
        angle = self.__c.get_angle()
        
        if 90 in hits:
            angle = 180 - angle
        if 0 in hits:
            angle = - angle
        return angle


class circle_inter:
    
    def __position_difference(self):
        pos1 = self.__c1.get_position()
        pos2 = self.__c2.get_position()
        
        x_diff = pos2[0] - pos1[0]
        y_diff = pos2[1] - pos1[1]
        
        return [x_diff, y_diff]
    
    def __init__(self, circle1, circle2):
        self.__c1 = circle1
        self.__c2 = circle2
        pos_diff = self.__position_difference()
        self.__x_diff = pos_diff[0]
        self.__y_diff = pos_diff[1]
        
    def overlap(self):
        center_distance = (self.__x_diff**2 + self.__y_diff**2)**(1/2)
        
        r1 = self.__c1.get_radius()
        r2 = self.__c2.get_radius()

        if center_distance <= r1 + r2:
            return True
        
        return False
    
    def __center_distance_angle(self):
        trng = np.degrees(np.arctan(abs(self.__y_diff) / abs(self.__x_diff)))
        if self.__x_diff > 0 and self.__y_diff > 0:
            angle = trng
        elif self.__x_diff < 0 and self.__y_diff > 0:
            angle = 180 - trng
        elif self.__x_diff < 0 and self.__y_diff < 0:
            angle = 270 - (90 - trng)
        elif self.__x_diff > 0 and self.__y_diff < 0:
            angle = 360 - trng

        return angle
    
    def outgoing_angles(self):
        outgoing_angles = []
        for circle in [self.__c1, self.__c2]:
            cross_section_tangent_angle = self.__center_distance_angle() + 90
            t_angle = cross_section_tangent_angle
            outgoing_angles.append(2*t_angle - circle.get_angle())
        return outgoing_angles


class circle_behavior:
    
    def __init__(self, circle1, circle2):
        self.__c1 = circle1
        self.__c2 = circle2
    
    def __set_new_angles(self):
        itr = circle_inter(self.__c1, self.__c2)
        self.__c1.set_angle(itr.outgoing_angles()[0])
        self.__c2.set_angle(itr.outgoing_angles()[1])
    
    def __define_superior_and_inferior(self, superior, inferior):
        self.__superior = superior
        self.__inferior = inferior
    
    def __valid_superior(self):
        if self.__c1.get_aggressivity() > self.__c2.get_aggressivity():
            self.__define_superior_and_inferior(self.__c1, self.__c2)
            return True
            
        elif self.__c1.get_aggressivity() < self.__c2.get_aggressivity():
            self.__define_superior_and_inferior(self.__c2, self.__c1)
            return True
        
        else:
            return False
            
    def __consume_inferior(self):
        self.__superior.add_area(self.__inferior.area())
        self.__inferior.set_radius(0)

    def set_new_properties(self):
        if self.__valid_superior():
            self.__consume_inferior()
        else:
            self.__set_new_angles()

    