import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5 * x

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

reg1 = np.polyfit(x, f(x), deg =1)
reg2 = np.polyfit(x, f(x), deg =7)

ry1 = np.polyval(reg1, x)
ry2 = np.polyval(reg2, x)

plt.plot(x, f(x), 'k', label= 'f(x)')
plt.plot(x, ry1, 'b^', label='regression = 1')
plt.plot(x, ry2, 'ro', label='regression = 7')

plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
