import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
cos = np.load("task7_cos.npy")
sin = np.load("task7_sin.npy")

plt.plot(x, sin, label="sin(x)")
plt.plot(x, cos, label="cos(x)")
plt.legend()

plt.show()