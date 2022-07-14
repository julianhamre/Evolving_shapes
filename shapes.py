#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np
import matplotlib.pyplot as plt

class circle:
    __speed = 2
    
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
    
    def move(self, direction_angle, time):
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
    

class interaction:

    def circle_with_border(self, circle, border):
        horizontal = 0
        vertical = 90
        hits = []
        
        cx = circle.get_position()[0]
        cy = circle.get_position()[1]
        cr = circle.get_radius()
        bx = border.get_position()[0]
        by = border.get_position()[1]
        bs = border.get_side()
        
        if cx + cr >= bx + bs:
            hits.append(vertical)
        
        if cy + cr >= by + bs:
            hits.append(horizontal)
        
        if cx - cr <= bx:
            hits.append(vertical)
        
        if cy - cr <= by:
            hits.append(horizontal)
        
        return hits


class show:

    def __init__(self):
        fig = plt.figure()
        self.ax = fig.add_subplot()
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        self.ax.set_aspect("equal", adjustable="box")
    
    def circle(self, circle):
        x = circle.get_position()[0]
        y = circle.get_position()[1]
        radius = circle.get_radius()
        self.__plot_circle = plt.Circle((x, y), radius)
        self.ax.add_patch(self.__plot_circle)
    
    def remove_circle(self):
        self.__plot_circle.remove()
    
    def border(self, border):
        crns = border.get_corners()
        self.ax.plot(crns[0], crns[1])


class manager:
    __time_interval = 0.1
    __itr = interaction()
    __show = show()
    __show_plot = True
    
    def __init__(self, circle, border):
        self.__c = circle
        self.__b = border
    
    def set_time_interval(self, interval):
        self.__time_interval = interval
    
    def set_show_plot(self, bool):
        self.__show_plot = bool
        
    def __border_interaciton_outcome(self, circle, border_hit):
        if len(border_hit) > 0:
            if 90 in border_hit:
                circle.set_angle(180 - circle.get_angle())
            if 0 in border_hit:
                circle.set_angle(- circle.get_angle())
    
    def __draw_and_reomve_circle(self):
        self.__show.circle(self.__c)
        plt.draw()
        plt.pause(0.01)
        self.__show.remove_circle()
    
    def emit(self, angle, time):
        self.__c.set_angle(angle)
        
        if self.__show_plot:
            self.__show.border(self.__b)
        
        for _ in range(int(time / self.__time_interval)):
            if self.__show_plot:
                self.__draw_and_reomve_circle()
            
            border_hit = self.__itr.circle_with_border(self.__c, self.__b)
            self.__border_interaciton_outcome(self.__c, border_hit)    
        
            self.__c.move(self.__c.get_angle(), self.__time_interval)
        
        if self.__show_plot:
            plt.show()

