import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

spread = np.random.rand(50)*100
center = np.ones(25)*50

outlier_high = np.random.rand(10)*100+100
outlier_low = np.random.rand(10)* -100
data = np.concatenate((spread,center,outlier_high,outlier_low),0)

ax.boxplot(data)
fig.show()