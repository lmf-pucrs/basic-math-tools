import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

def f(x):
    return np.sin(x) * 0.5 * x

x = np.linspace(-2 * np.pi, 2 * np.pi, 25)

ipo = spi.splrep(x, f(x), k=1)
iy = spi.splev(x, ipo)

plt.plot(x, f(x), 'k', label='f(x)')
plt.plot(x, iy, 'y--', label='interpolation')

plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()
