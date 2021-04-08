#!/usr/bin/env /home/sree/miniconda3/bin/python3.8
#------------------------------------------------------------------------------
# This script reads data from files named dis_scn.dat and dis_ocn.dat
# and creates arrays which contain the data that can be plotted at will at a
# later point of time.
#------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import seaborn as sns
import os
import re

from matplotlib.lines import Line2D
from matplotlib.backends.backend_pdf import PdfPages
#pp = PdfPages('order-param.pdf')
pp = PdfPages('order_par_hist.pdf')

n = np.size(glob.glob('./reac-distances/*_oc*.dat'))
print(n)
oc_dis = [pd.read_csv(infile, header=None) for infile in sorted(glob.glob('./reac-distances/*_oc*.dat'))]
sc_dis = [pd.read_csv(infile, header=None) for infile in sorted(glob.glob('./reac-distances/*_sc*.dat'))]

f, ax = plt.subplots()
custom_lines = [Line2D([0], [0], color='k'),
                Line2D([0], [0], color='k', linestyle = '--')]

snaps = np.arange(501)

print(sc_dis[1])
ax = sns.histplot(oc_dis[2]-sc_dis[2], bins = 10, legend=False)
#ax = sns.histplot(oc_dis[1]-sc_dis[1], bins = 10)

# ax.legend(custom_lines, ['S--C distance', 'O--C distance'])
ax.set_xlabel('dis(O-C)-dis(S-C)')
ax.set_ylabel('Count')
pp.savefig()
pp.close()
