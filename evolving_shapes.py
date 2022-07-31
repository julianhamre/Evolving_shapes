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


def interaction_circle_with_circles(circle_index, circles):
    c1 = circles[circle_index]
    for i in range(circle_index, len(circles) - 1):
        c2 = circles[i + 1]
        itr = interaction.circle(c1, c2)
        if itr.overlap():
            bh = interaction.behavior(c1, c2)
            bh.set_all_new()
            
def interaction_circle_with_border(border, circle):
    itr = interaction.border(border, circle)
    hits = itr.hits()
    if len(hits) > 0:
        new_angle = itr.outgoing_angle()
        circle.set_angle(new_angle)


class _random_circles:
    
    def __init__(self, border):
        self.__b = border
    
    def __random_position(self, radius, position_index):
        minimum = self.__b.get_position()[position_index] + radius
        maximum = minimum + self.__b.get_side() - 2*radius
        return uniform(minimum, maximum)

    def __remove_overlapping_circle(self, circles):
        c = circles[0]
        first_ang = c.get_angle()
        interaction_circle_with_circles(0, circles)
        second_ang = c.get_angle()
        if first_ang != second_ang:
            circles.remove(c)
        return circles

    def fabricate(self, number_of_circles):
        circles = []
        radius = 1
        while len(circles) < number_of_circles:
            x = self.__random_position(radius, 0)
            y = self.__random_position(radius, 1)
            c = shapes.circle(radius, x, y)
            angle = uniform(0, 360)
            c.set_angle(angle)
            circles.insert(0, c) 
            circles = self.__remove_overlapping_circle(circles)
        return circles


class manager:
    __time_interval = 0.1
    __show = show()
    __show_plot = True
    __b = shapes.border(18, 1, 1)
    
    def set_time_interval(self, interval):
        self.__time_interval = interval
        
    def set_border(self, border):
        self.__b = border
    
    def show_plot(self, bool):
        self.__show_plot = bool
        
    def random_circles(self, number_of_circles):
        rnd = _random_circles(self.__b)
        return rnd.fabricate(number_of_circles)

    def emit(self, circles, time):
        if self.__show_plot:
            self.__show.border(self.__b)
        
        for _ in range(int(time / self.__time_interval)):
            if self.__show_plot:
                self.__show.draw_and_erase_circles(circles)
            
            circle_index = 0
            
            for circle in circles:
                interaction_circle_with_circles(circle_index, circles)
                interaction_circle_with_border(self.__b, circle)
                circle.move(self.__time_interval)
                circle_index += 1
                
        if self.__show_plot:
            self.__show.view_all()