import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

#linspace creates an array of length 5, evenly spacing numbers between stop & start
x = np.linspace(0,2*np.pi,400)
y = np.sin(x)
fig, ax = plt.subplots()
#Sets the x and y-axis
ax.set_xlim(0,800)
ax.set_ylim(0,800)
#hides axis
ax.set_axis_off()


#(position, width, height)
box_left = patches.Rectangle((100, 300), 50, 50, color="deepskyblue")
box_right = patches.Rectangle((300, 300), 50, 50, color="orangered")
#draws the boxes
ax.add_patch(box_left)
ax.add_patch(box_right)

def update(frame):
    
plt.show()
