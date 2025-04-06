import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#linspace creates an array of length 5, evenly spacing numbers between stop & start
x = np.linspace(0,2*np.pi,400)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)

