import numpy as np
import matplotlib.pyplot as plt

rand = np.random.random(100000)*10.0+35.0
error = 5.0
ds = np.array([61,115,31,177])

plt.hist(rand)
plt.show()

