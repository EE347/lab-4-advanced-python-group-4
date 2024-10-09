import numpy as np


x = np.linspace(0, 10, 101)
print(x)

cos_values = np.cos(x)
sin_values = np.sin(x)

np.save("task7_sin.npy", sin_values)
np.save("task7_cos.npy", cos_values)