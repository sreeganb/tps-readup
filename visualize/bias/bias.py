#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
from scipy.stats import skewnorm



my_palette = ['#355EE7', '#CB201A', '#1E9965', '#D291BC', '#FA8B1D','#875C36', '#FEB301']
sns.set(style = "ticks", context = "paper")
sns.set_palette(sns.color_palette(my_palette))

plt.rc('text', usetex=True)
plt.rc('xtick', labelsize = 7)
plt.rc('ytick', labelsize = 7)
plt.rc('axes', labelsize = 7)

width = 3.386
height = width/1.31

# 100 linearly spaced numbers
x = np.linspace(-5.0,9.0,400)
a = 4
#x = np.linspace(skewnorm.ppf(0.01, a),skewnorm.ppf(8000, a), 100)
fcons = 100
alp = 0.10
pre = 8000
xref = 6.0
# the function, which is y = x^2 here
y1 = 0.5*fcons*(x-xref)**2
y2 = pre*np.exp(-alp*(x-0.5)**2)
y3 = y2 + y1
# setting the axes at the centre
fig, ax = plt.subplots()
fig.set_size_inches(width, height)
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y2, label = 'Free energy', lw =1, ls = 'dotted')
plt.plot(x,y1, label = 'Harmonic bias', lw=1, ls='dashed')
plt.plot(x,y3, label = 'Biased free energy', lw=1, ls = 'dashdot')
#ax.fill_between(x,y3,0,color = 'green', alpha = 0.1)
plt.yticks([])
plt.xlabel(r'$\xi$')
plt.ylabel(r'$W(\xi)$')
ax.legend(fontsize = 7)
# show the plot
#plt.show()
plt.savefig('energy-bias.eps', dpi = 1000)
