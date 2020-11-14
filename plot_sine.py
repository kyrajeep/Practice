#from https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html
# plot a sine curve
import numpy as np
import matplotlib.pylab as plt
x = np.linspace(-np.pi, np.pi, 200)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()