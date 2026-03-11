import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 400)
y = np.linspace(-6, 6, 400)
X, Y = np.meshgrid(x, y)

Z1 = X**2 + X*Y**2 - 11
Z2 = Y**2 + 4*X*Y - 28

plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of f1(x,y)=0 (red) and f2(x,y)=0 (blue)')
plt.show()
