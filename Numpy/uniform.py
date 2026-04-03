import numpy as np
from scipy import stats

#Create an array containing 800 random floats between 0 and 5:

array = np.random.uniform(0.0,5.0,800)
print(array)
#Create an array containing 1000 random int between 0 and 10:
array2 = np.random.uniform(0,10,1000)
print(array2)

avg = np.mean(array2)
print(f"Mean of these : ${avg}")
median = np.median(array2)
print(f"Median of these : ${median}")
spreadValue = np.std(array2)
print(f"Spread Value: ${spreadValue}")
