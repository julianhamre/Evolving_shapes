#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:55:56 2022

@author: julianhamre
"""

import shapes as sh

b = sh.border(18, 1, 1)
m = sh.manager(b)
#m.set_show_plot(False)
circles = m.random_circles(10)
m.emit(circles, 10)