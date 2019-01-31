import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('shiyanlou')

ax.plot(x,x**(1/8),'b--',label=r'$y=x^{1/8}$')
ax.plot(x,x**8,'r--',label=r'$y=x^{8}$')
ax.plot(x,x**(1/2),'r.',label=r'$y=x^{1/2}$')
ax.plot(x,x**2,'b.',label=r'$y=x^{2}$')
ax.plot(x,x,'g-',label='r$y=x$')

ax.legend()
ax.axis([0,1,0,1])