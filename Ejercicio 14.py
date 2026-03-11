import numpy as np
import matplotlib.pyplot as plt

# Define the equations for contour plotting
x = np.linspace(-3, 8, 400)
y = np.linspace(-3, 8, 400)
X, Y = np.meshgrid(x, y)

F1 = (X - 4)**2 + (Y - 4)**2 - 16
F2 = X**2 + Y**2 - 6

plt.figure(figsize=(6,6))
plt.contour(X, Y, F1, levels=[0], colors='blue', label='Eq 1')
plt.contour(X, Y, F2, levels=[0], colors='red', label='Eq 2')
plt.grid(True)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title('Graphical Solution')
plt.show()
