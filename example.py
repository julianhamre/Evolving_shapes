#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:55:56 2022

@author: julianhamre
"""

import evolving_shapes as ev

b = ev.shapes.border(18, 1, 1)
m = ev.manager(b)
#m.show_plot(False)
circles = m.random_circles(5)
m.emit(circles, 20)