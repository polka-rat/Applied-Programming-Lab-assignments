import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms

fig,ax = plt.subplots(figsize=(13,4))
# self.ax.pcolormesh(self.maze, cmap=cmap)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-1,15)
ax.set_ylim(-1,5)

import pylab
NUM_COLORS = 100


plt.tight_layout()
plt.gca().invert_yaxis()

cm = pylab.get_cmap('seismic')
for i in range(NUM_COLORS):
    color = cm(1.*i/NUM_COLORS)  # color will now be an RGBA tuple

    rect = Rectangle((0.1*i,0.1*i), 0.25, 0.5, facecolor=color, alpha=0.9,edgecolor='black')
    ax.text(0.5+0.125,0.5+0.25,'a',horizontalalignment='center',verticalalignment='center')
    ax.add_patch(rect)
ax.text(.2, .5, 'round', bbox=dict(boxstyle='round', fc="w", ec="k"),
    transform=ax.transAxes, size="large", color="tab:blue",
    horizontalalignment="right", verticalalignment="center")
plt.show()


styles = mpatch.BoxStyle.get_styles()
print(styles['round'])