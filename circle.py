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


class show:
        
    def movement(self, radius, all_positions):
        pts = all_positions
        for i in range(len(pts[0])):
            c = circle(radius, pts[0][i], pts[1][i])
            plt.xlim(0, 20)
            plt.ylim(0, 20)
            plt.plot(c.get_points()[0], c.get_points()[1])
            plt.show()
