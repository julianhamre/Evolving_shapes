#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:55:56 2022

@author: julianhamre
"""

import evolving_shapes as ev


m = ev.manager()
#m.show_plot(False)
circles = m.random_circles(5)
aggresive_circle = ev.shapes.circle(1, 3, 3)
aggresive_circle.set_color("red")
aggresive_circle.set_aggressivity(1)
circles.append(aggresive_circle)
m.emit(circles, 20)