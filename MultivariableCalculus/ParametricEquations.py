# Imports
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-10, 10, 0.01)

# Blanket pattern
x = np.sin(t*9)
y = np.sin(t*10)
plt.plot(x, y)
plt.show()

# Galactic Star
x = np.cos(t * 10)*2.3 + np.cos(t * 23)
y = np.sin(t * 10)*2.3 - np.sin(t * 23)
plt.plot(x, y)
plt.show()