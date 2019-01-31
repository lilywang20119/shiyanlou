import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.arange(1,101)
y = 20+3*x + np.random.normal(0,60,100)
ax.scatter(x,y)
fig.show()