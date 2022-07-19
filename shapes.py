#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np
import matplotlib.pyplot as plt
from random import uniform

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
    
    def border_outcome(self, circle, border_hit):
        if len(border_hit) > 0:
            if 90 in border_hit:
                circle.set_angle(180 - circle.get_angle())
            if 0 in border_hit:
                circle.set_angle(- circle.get_angle())
    
    def circle_with_circle(self, circle1, circle2):
        pos1 = circle1.get_position()
        pos2 = circle2.get_position()
        
        x_diff = pos1[0] - pos2[0]
        y_diff = pos1[1] - pos2[1]
        
        center_distance = (x_diff**2 + y_diff**2)**(1/2)
        
        r1 = circle1.get_radius()
        r2 = circle2.get_radius()

        if center_distance <= r1 + r2:
            return True
        
        return False
    
    def circle_with_circles(self, circle_index, circles):
        c1 = circles[circle_index]
        for i in range(circle_index, len(circles) - 1):
            c2 = circles[i + 1]
            if self.circle_with_circle(c1, c2):
                c1.set_angle(0)
                c2.set_angle(180)


class show:
    __plot_circles_shown = []
    
    def __init__(self):
        fig = plt.figure()
        self.ax = fig.add_subplot()
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        self.ax.set_aspect("equal", adjustable="box")
    
    def circles(self, circles):
        for circle in circles:
            x = circle.get_position()[0]
            y = circle.get_position()[1]
            radius = circle.get_radius()
            plot_circle = plt.Circle((x, y), radius)
            self.ax.add_patch(plot_circle)
            self.__plot_circles_shown.append(plot_circle)
    
    def remove_circles(self):
        for plot_circle in self.__plot_circles_shown:
            plot_circle.remove()
        self.__plot_circles_shown = []
    
    def border(self, border):
        crns = border.get_corners()
        self.ax.plot(crns[0], crns[1])


class manager:
    __time_interval = 0.1
    __itr = interaction()
    __show = show()
    __show_plot = True
    
    def __init__(self, border):
        self.__b = border
    
    def set_time_interval(self, interval):
        self.__time_interval = interval
    
    def set_show_plot(self, bool):
        self.__show_plot = bool

    def __random_position(self, radius, position_index):
        minimum = self.__b.get_position()[position_index] + radius
        maximum = + self.__b.get_side() - 2*radius
        return uniform(minimum, maximum)

    def random_circles(self, number_of_circles):
        circles = []
        radius = 1
        for _ in range(number_of_circles):
            x = self.__random_position(radius, 0)
            y = self.__random_position(radius, 1)
            c = circle(radius, x, y)
            angle = uniform(0, 360)
            c.set_angle(angle)
            circles.append(c) 
        return circles

    def draw_and_remove_circles(self, circles):
        self.__show.circles(circles)
        plt.draw()
        plt.pause(0.01)
        self.__show.remove_circles()

    def emit(self, circles, time):
        if self.__show_plot:
            self.__show.border(self.__b)
        
        for _ in range(int(time / self.__time_interval)):
            if self.__show_plot:
                self.draw_and_remove_circles(circles)
            
            circle_index = 0
            
            for circle in circles:
                self.__itr.circle_with_circles(circle_index, circles)
                border_hit = self.__itr.circle_with_border(circle, self.__b)
                self.__itr.border_outcome(circle, border_hit)
                circle.move(circle.get_angle(), self.__time_interval)
                circle_index += 1
                
        if self.__show_plot:
            plt.show()

