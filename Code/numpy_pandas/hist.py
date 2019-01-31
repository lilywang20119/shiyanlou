import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = np.random.normal(0,20,1000)
bins = np.arange(-100,100,5)
ax.hist(data,bins=bins)
fig.show()