#!/usr/bin/env python3.8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 

my_palette = ['#355EE7', '#CB201A', '#1E9965', '#D291BC', '#875C36', '#FEB301']
sns.set(context="paper", style = "ticks", font_scale = 1.6)

sns.set_palette(sns.color_palette(my_palette))

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('traj1.pdf')

f, ax = plt.subplots()

#df1=pd.read_csv("5_dis_c-s.csv")
#df2=pd.read_csv('5_dis_c-o.csv')
df1=pd.read_csv("4-c-s.csv")
df2=pd.read_csv('4-c-o.csv')

legends=["C-S", "C-O"]

x = list(range(0, 249))
y1 = np.ones(250)
y2 = np.ones(250)
y1 = df1
y2 = df2

print(np.mean(y1),np.mean(y2))

l1 = ax.plot(x, y1, marker = 'o', markersize = 2, linewidth = 2)
l2 = ax.plot(x, y2, marker = 'v', markersize = 2, linewidth = 2)
ax.set_yticks(np.arange(1.5,4.0,0.1), minor=True)
ax.set_xlabel('Time slice')
ax.set_ylabel('Distance' r'$(\AA)$')
#ax[0,0].set_yticks([5, 7, 9, 11], minor = True)

f.legend(legends, frameon = True, fancybox = True, loc = 'upper right', framealpha = 0.5)

pp.savefig()
#pp.savefig(bbox_extra_artists = (leg))
pp.close()
