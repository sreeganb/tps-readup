#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math

# 100 linearly spaced numbers
x = np.linspace(-5,8,100)

fcons = 20
alp = 0.50
pre = 1000
xref = 3.0
# the function, which is y = x^2 here
y1 = fcons*(x-xref)**2
y2 = pre*np.exp(-alp*x**2)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y1, 'r')
plt.plot(x,y2, 'b')
# show the plot
plt.show()
