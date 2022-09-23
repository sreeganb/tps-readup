#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math

my_palette = ['#355EE7', '#CB201A', '#1E9965', '#D291BC', '#FA8B1D','#875C36', '#FEB301']
sns.set(style = "ticks", context = "paper")
sns.set_palette(sns.color_palette(my_palette))

plt.rc('text', usetex=True)
plt.rc('xtick', labelsize = 8)
plt.rc('ytick', labelsize = 8)
plt.rc('axes', labelsize = 8)

width = 3.386
height = width/1.31

# 100 linearly spaced numbers
x = np.linspace(-5,8,100)

fcons = 100
alp = 0.10
pre = 8000
xref = 6.0
# the function, which is y = x^2 here
y1 = 0.5*fcons*(x-xref)**2
y2 = pre*np.exp(-alp*x**2)
y3 = y2 + y1
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y1, label = 'Harmonic bias')
plt.plot(x,y2, label = 'Global free energy')
plt.plot(x,y3, label = 'Biased energy')
#ax.fill_between(x,y3,0,color = 'green', alpha = 0.1)
plt.yticks([])
ax.legend()
# show the plot
#plt.show()
plt.savefig('energy-bias.png', dpi = 800)
