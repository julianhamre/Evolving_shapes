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

    def move_in_intervals(self, direction_angle, time, intervals):
        time_points = np.linspace(0, time, intervals)
        x = []
        y = []
        element_distance = time_points[1] - time_points[0]
        for i in range(len(time_points)):
            self.move(direction_angle, element_distance)
            x.append(self.x)
            y.append(self.y)
        all_positions = [x, y]
        return all_positions

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
        pts = circle.get_points()
        self.ax.plot(pts[0], pts[1])
    
    def border(self, border):
        crns = border.get_corners()
        self.ax.plot(crns[0], crns[1])
    
    def movement(self, radius, all_positions):
        pts = all_positions
        for i in range(len(pts[0])):
            c = circle(radius, pts[0][i], pts[1][i])
            self.ax.plot(c.get_points()[0], c.get_points()[1])


class manager:
    time_interval = 0.1
    itr = interaction()
    show = show()
    
    def __init__(self, circle, border):
        self.c = circle
        self.b = border
    
    def set_time_interval(self, interval):
        self.time_interval = interval
    
    def emit(self, angle, time):
        self.angle = angle
        
        for _ in range(int(time / self.time_interval)):
            self.show.border(self.b)
            self.show.circle(self.c)
            
            border_hit = self.itr.circle_with_border(self.c, self.b)
            
            if len(border_hit) > 0:
                if 90 in border_hit:
                    self.angle = 180 - self.angle
                if 0 in border_hit:
                    self.angle = - self.angle 
                
            self.c.move(self.angle, self.time_interval)

