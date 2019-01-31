import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.random.randn(100)
y = np.random.randn(100)

ax.plot(x,y)
fig.show()