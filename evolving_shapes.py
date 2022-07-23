#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:50:52 2022

@author: julianhamre
"""

from graphic import show
import shapes
import interaction
from random import uniform


class manager:
    __time_interval = 0.1
    __show = show()
    __show_plot = True
    
    def __init__(self, border):
        self.__b = border
    
    def set_time_interval(self, interval):
        self.__time_interval = interval
    
    def show_plot(self, bool):
        self.__show_plot = bool

    def __random_position(self, radius, position_index):
        minimum = self.__b.get_position()[position_index] + radius
        maximum = minimum + self.__b.get_side() - 2*radius
        return uniform(minimum, maximum)

    def random_circles(self, number_of_circles):
        circles = []
        radius = 1
        for _ in range(number_of_circles):
            x = self.__random_position(radius, 0)
            y = self.__random_position(radius, 1)
            c = shapes.circle(radius, x, y)
            angle = uniform(0, 360)
            c.set_angle(angle)
            circles.append(c) 
        return circles

    def __interaction_circle_with_circles(self, circle_index, circles):
        c1 = circles[circle_index]
        for i in range(circle_index, len(circles) - 1):
            c2 = circles[i + 1]
            itr = interaction.circle(c1, c2)
            if itr.overlap():
                new_angles = itr.outgoing_angles()
                c1.set_angle(new_angles[0])
                c2.set_angle(new_angles[1])
                
    def __interaction_circle_with_border(self, circle):
        itr = interaction.border(self.__b, circle)
        hits = itr.hits()
        if len(hits) > 0:
            new_angle = itr.outgoing_angle()
            circle.set_angle(new_angle)

    def emit(self, circles, time):
        if self.__show_plot:
            self.__show.border(self.__b)
        
        for _ in range(int(time / self.__time_interval)):
            if self.__show_plot:
                self.__show.draw_and_erase_circles(circles)
            
            circle_index = 0
            
            for circle in circles:
                self.__interaction_circle_with_circles(circle_index, circles)
                self.__interaction_circle_with_border(circle)
                circle.move(self.__time_interval)
                circle_index += 1
                
        if self.__show_plot:
            self.__show.view_all()