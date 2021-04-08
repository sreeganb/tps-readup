#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 

#==============================================================================
# Seaborn to make the graph look pretty
#==============================================================================
#flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
#sns.set_palette(flatui)
#sns.palplot(color_palette(flatui))
my_palette = ['#355EE7', '#CB201A', '#1E9965', '#D291BC', '#875C36', '#FEB301']
sns.set(context="paper", style = "ticks", font_scale = 2.2)
sns.set_palette(sns.color_palette(my_palette))
#sns.palplot(sns.color_palette())
#current_palette = sns.color_palette()
#sns.palplot(current_palette)
#==============================================================================

#==============================================================================
# Easy way to get pdf figure outputs
#==============================================================================
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('new-bas_conv.pdf')

#from matplotlib.pyplot import figure
#figure(num=None, figsize=(10, 4), dpi=300, facecolor='w', edgecolor='k')

f, ax = plt.subplots(2, 2, figsize=(10,7), constrained_layout=False, sharex = 'col')

legends=["GKS-spRPA","HF","PBE","PBE0", "MP2", "CC2"]

df = pd.read_csv('svpd_lif.csv', sep = ",", header = 0)
df_1 = pd.read_csv('svp_lif.csv', sep = ",", header = 0)
df_2 = pd.read_csv('svp_hcn.csv', sep = ",", header = 0)
df_3 = pd.read_csv('svpd_hcn.csv', sep = ",", header = 0)
x_1 = ["SVPD", "TZVPPD", "QZVPPD"]
x_2 = ["SVP", "TZVPP", "QZVPP"]
x1 = [1, 2, 3]

y1 = df_1["rpa"]
y2 =df_1["hf"]
y3 =df_1["pbe"]
y4 =df_1["pbe0"]
y5 =df_1["mp2"]
y6 =df_1["cc2"]

l1 = ax[0,0].plot(x1, y1, marker = 'o', markersize = 6, linewidth = 2)
l2 = ax[0,0].plot(x1, y2, marker = 'v', markersize = 6, linewidth = 2)
l3 = ax[0,0].plot(x1, y3, marker = 'H', markersize = 6, linewidth = 2)
l4 = ax[0,0].plot(x1, y4, marker = '^', markersize = 6, linewidth = 2)
l5 = ax[0,0].plot(x1, y5, marker = 'D', markersize = 6, linewidth = 2)
l6 = ax[0,0].plot(x1, y6, marker = 's', markersize = 6, linewidth = 2)

ax[0,0].set_xticks(x1)
ax[0,0].set_xticklabels(x_2)
ax[0,0].set_yticks(np.arange(4,14,2))
ax[0,0].set_yticks([5, 7, 9, 11], minor = True)
ax[0,0].set_ylabel(r"$\alpha_{iso}$(LiF), a. u.")

y1 = df["rpa"]
y2 =df["hf"]
y3 =df["pbe"]
y4 =df["pbe0"]
y5 =df["mp2"]
y6 =df["cc2"]
ax[0,1].plot(x1, y1, marker = 'o', markersize = 6, linewidth = 2)
ax[0,1].plot(x1, y2, marker = 'v', markersize = 6, linewidth = 2)
ax[0,1].plot(x1, y3, marker = 'H', markersize = 6, linewidth = 2)
ax[0,1].plot(x1, y4, marker = '^', markersize = 6, linewidth = 2)
ax[0,1].plot(x1, y5, marker = 'D', markersize = 6, linewidth = 2)
ax[0,1].plot(x1, y6, marker = 's', markersize = 6, linewidth = 2)
ax[0,1].set_xticks(x1)
ax[0,1].set_xticklabels(x_1)
ax[0,1].set_yticks(np.arange(6,14,2))
ax[0,1].set_yticks([7, 9, 11, 13], minor = True)
#ax[0,1].legend(legends, frameon = True, fancybox = True, ncol=3, loc = 'upper center', bbox_to_anchor = (-0.0,1.41), framealpha = 0.5)
#ax[0,1].legend(legends)

y1 = df_2["rpa"]
y2 =df_2["hf"]
y3 =df_2["pbe"]
y4 =df_2["pbe0"]
y5 =df_2["mp2"]
y6 =df_2["cc2"]
ax[1,0].plot(x1, y1, marker = 'o', markersize = 6, linewidth = 2)
ax[1,0].plot(x1, y2, marker = 'v', markersize = 6, linewidth = 2)
ax[1,0].plot(x1, y3, marker = 'H', markersize = 6, linewidth = 2)
ax[1,0].plot(x1, y4, marker = '^', markersize = 6, linewidth = 2)
ax[1,0].plot(x1, y5, marker = 'D', markersize = 6, linewidth = 2)
ax[1,0].plot(x1, y6, marker = 's', markersize = 6, linewidth = 2)
ax[1,0].set_ylabel(r"$\alpha_{iso}(HCN)$, a. u.")
ax[1,0].set_xticks(x1)
ax[1,0].set_xticklabels(x_2)
ax[1,0].set_yticks(np.arange(11,17,2))
ax[1,0].set_yticks([12, 14, 16], minor = True)

y1 = df_3["rpa"]
y2 =df_3["hf"]
y3 =df_3["pbe"]
y4 =df_3["pbe0"]
y5 =df_3["mp2"]
y6 =df_3["cc2"]
ax[1,1].plot(x1, y1, marker = 'o', markersize = 6, linewidth = 2)
ax[1,1].plot(x1, y2, marker = 'v', markersize = 6, linewidth = 2)
ax[1,1].plot(x1, y3, marker = 'H', markersize = 6, linewidth = 2)
ax[1,1].plot(x1, y4, marker = '^', markersize = 6, linewidth = 2)
ax[1,1].plot(x1, y5, marker = 'D', markersize = 6, linewidth = 2)
ax[1,1].plot(x1, y6, marker = 's', markersize = 6, linewidth = 2)
ax[1,1].set_xticks(x1)
ax[1,1].set_xticklabels(x_1)
ax[1,1].set_yticks(np.arange(15,18,1))
ax[1,1].set_yticks([15.5, 16.5, 17.5], minor = True)

#f.legend(legends)
f.legend(legends, frameon = True, fancybox = True, ncol=3, loc = 'upper center', bbox_to_anchor = (0.5,1.015), framealpha = 0.5)
#f.legend(legends, frameon = True, fancybox = True, loc = 'upper right', bbox_to_anchor = (1.2,1.0), framealpha = 0.5)
#plt.tight_layout()

pp.savefig()
#pp.savefig(bbox_extra_artists = (leg))
pp.close()
