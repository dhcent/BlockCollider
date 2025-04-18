import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

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

#Velocity in m/s
velocity = 1
fps = 30
dt = 1/fps
pos_x_left = 100

def update(frame):
    global pos_x_left, box_left
    pos_x_left += velocity * dt
    box_left.set_x(pos_x_left)
    #update expects tuple return
    return box_left,

#interval is delay between frames in ms; 500 m/s between each frame,
ani = FuncAnimation(fig, update, frames=100, interval=1000/fps, blit=True)
plt.show()

# y = lambda x: 4*x**2 + 7*x + 1
#
# a = np.linspace(-5,5,10)
# b = np.array([-72,-82,-49,-33,-8,7,4,72,186,490])
#
#
# plt.scatter(a,b)
# plt.show()