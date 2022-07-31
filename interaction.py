#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:02:00 2022

@author: julianhamre
"""

import numpy as np


class border:

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
        if 90 in hits:
            self.__c.set_angle(180 - self.__c.get_angle())
        if 0 in hits:
            self.__c.set_angle(- self.__c.get_angle())
        return self.__c.get_angle()


class circle:
    
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
    

class status:
    
    def __init__(self, circle1, circle2):
        self.__c1 = circle1
        self.__c2 = circle2
    
    def superior(self):
        if self.__c1.get_aggressivity() > self.__c2.get_aggressivity():
            return self.__c1
        elif self.__c1.get_aggressivity() == self.__c2.get_aggressivity():
            return 0
        else:
            return self.__c2
        

class behavior:
    
    def __init__(self, circle1, circle2):
        self.__c1 = circle1
        self.__c2 = circle2
        self.__status = status(self.__c1, self.__c2)
    
    def set_new_angles(self):
        itr = circle(self.__c1, self.__c2)
        self.__c1.set_angle(itr.outgoing_angles()[0])
        self.__c2.set_angle(itr.outgoing_angles()[1])
    
    def set_aggressivity_outcome(self):
        if self.__status.superior() == self.__c1:
            self.__c2.set_aggressivity(self.__c1.get_aggressivity())
            self.__c2.set_color(self.__c1.get_color())
        elif self.__status.superior() == self.__c2:
            self.__c1.set_aggressivity(self.__c2.get_aggressivity())
            self.__c1.set_color(self.__c2.get_color())
           
            
    def set_all_new(self):
        self.set_new_angles()
        self.set_aggressivity_outcome()

    