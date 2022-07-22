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
    

class border_interaction:

    def __init__(self, border, circle):
        self.b = border
        self.c = circle
    
    def hits(self):
        horizontal = 0
        vertical = 90
        hits = []
        
        cx = self.c.get_position()[0]
        cy = self.c.get_position()[1]
        cr = self.c.get_radius()
        bx = self.b.get_position()[0]
        by = self.b.get_position()[1]
        bs = self.b.get_side()
        
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
            return 180 - self.c.get_angle()
        if 0 in hits:
            return - self.c.get_angle()


class circle_interaction:
    
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
    
    def __print_circle_angs(self):
        print("C1 ANG:", self.__c1.get_angle())
        print("C2 ANG:", self.__c2.get_angle())

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
        maximum = minimum + self.__b.get_side() - 2*radius
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

    def __interaction_circle_with_circles(self, circle_index, circles):
        c1 = circles[circle_index]
        for i in range(circle_index, len(circles) - 1):
            c2 = circles[i + 1]
            itr = circle_interaction(c1, c2)
            if itr.overlap():
                new_angles = itr.outgoing_angles()
                c1.set_angle(new_angles[0])
                c2.set_angle(new_angles[1])
                
    def __interaction_circle_with_border(self, circle):
        itr = border_interaction(self.__b, circle)
        hits = itr.hits()
        if len(hits) > 0:
            new_angle = itr.outgoing_angle()
            circle.set_angle(new_angle)
        circle.move(circle.get_angle(), self.__time_interval)

    def __draw_and_erase_circles(self, circles):
        self.__show.circles(circles)
        plt.draw()
        plt.pause(0.02)
        self.__show.remove_circles()

    def emit(self, circles, time):
        if self.__show_plot:
            self.__show.border(self.__b)
        
        for _ in range(int(time / self.__time_interval)):
            if self.__show_plot:
                self.__draw_and_erase_circles(circles)
            
            circle_index = 0
            
            for circle in circles:
                self.__interaction_circle_with_circles(circle_index, circles)
                self.__interaction_circle_with_border(circle)
                circle_index += 1
                
        if self.__show_plot:
            plt.show()
