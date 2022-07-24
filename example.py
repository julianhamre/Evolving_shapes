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
m.emit(circles, 20)