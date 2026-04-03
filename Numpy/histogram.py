import numpy as np
import matplotlib.pyplot as plt

array = np.random.uniform(0,10,200)

plt.hist(array,5)
plt.show()