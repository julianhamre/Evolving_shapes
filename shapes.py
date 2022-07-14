#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:20 2022

@author: julianhamre
"""

import numpy as np
import matplotlib.pyplot as plt

class circle:
    speed = 2
    
    def __init__(self, radius, x_coordinate, y_coordinate):
        self.radius = radius
        self.x = x_coordinate
        self.y = y_coordinate
    
    def move(self, direction_angle, time):
        distance = self.speed * time
        radians_angle = np.radians(direction_angle)
        self.x += np.cos(radians_angle) * distance
        self.y += np.sin(radians_angle) * distance

    def get_points(self):
        angles = np.linspace(0, 2*np.pi, 100)
        x = []
        y = []
        for angle in angles:
            x.append(self.radius * np.cos(angle) + self.x)
            y.append(self.radius * np.sin(angle) + self.y)
        return [x, y]


class border:
    
    def __init__(self, side_length, x_coordinate, y_coordinate):
        self.side = side_length
        
        # coordinates for bottom left corner
        self.x = x_coordinate
        self.y = y_coordinate

    def get_corners(self):
        x = self.x
        sx = x + self.side
        y = self.y
        sy = y + self.side
        
        x = [x, sx, sx, x, x]
        y = [y, y, sy, sy, y]

        return [x, y]
    

class interaction:

    def circle_with_border(self, circle, border):
        horizontal = 0
        vertical = 90
        hits = []
        
        if circle.x + circle.radius >= border.x + border.side:
            hits.append(vertical)
        
        if circle.y + circle.radius >= border.y + border.side:
            hits.append(horizontal)
        
        if circle.x - circle.radius <= border.x:
            hits.append(vertical)
        
        if circle.y - circle.radius <= border.y:
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
        self.plot_circle = plt.Circle((circle.x, circle.y), circle.radius)
        self.ax.add_patch(self.plot_circle)
    
    def remove_circle(self):
        self.plot_circle.remove()
    
    def border(self, border):
        crns = border.get_corners()
        self.ax.plot(crns[0], crns[1])


class manager:
    time_interval = 0.1
    itr = interaction()
    show = show()
    show_plot = True
    
    def __init__(self, circle, border):
        self.c = circle
        self.b = border
    
    def set_time_interval(self, interval):
        self.time_interval = interval
    
    def set_show_plot(self, bool):
        self.show_plot = bool
        
    def border_interaciton_outcome(self, border_hit):
        if len(border_hit) > 0:
            if 90 in border_hit:
                self.angle = 180 - self.angle
            if 0 in border_hit:
                self.angle = - self.angle 
    
    def emit(self, angle, time):
        self.angle = angle
        
        if self.show_plot:
            self.show.border(self.b)
        
        for _ in range(int(time / self.time_interval)):
            if self.show_plot:
                self.show.circle(self.c)
                plt.draw()
                plt.pause(0.01)
                self.show.remove_circle()
            
            border_hit = self.itr.circle_with_border(self.c, self.b)
        
            self.border_interaciton_outcome(border_hit)    
        
            self.c.move(self.angle, self.time_interval)
        
        if self.show_plot:
            plt.show()

