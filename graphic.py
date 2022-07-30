#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:05:49 2022

@author: julianhamre
"""

import matplotlib.pyplot as plt


class show:
    __plot_circles_shown = []
    
    def __init__(self):
        fig = plt.figure()
        self.__ax = fig.add_subplot()
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        self.__ax.set_aspect("equal", adjustable="box")
    
    def __circles(self, circles):
        for circle in circles:
            x = circle.get_position()[0]
            y = circle.get_position()[1]
            radius = circle.get_radius()
            plot_circle = plt.Circle((x, y), radius, color=circle.get_color())
            self.__ax.add_patch(plot_circle)
            self.__plot_circles_shown.append(plot_circle)
    
    def __remove_circles(self):
        for plot_circle in self.__plot_circles_shown:
            plot_circle.remove()
        self.__plot_circles_shown = []
        
    def draw_and_erase_circles(self, circles):
        self.__circles(circles)
        plt.draw()
        plt.pause(0.02)
        self.__remove_circles()
    
    def border(self, border):
        crns = border.get_corners()
        self.__ax.plot(crns[0], crns[1])
        
    def view_all(self):
        plt.show()
        
        