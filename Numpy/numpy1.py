import numpy as np
from scipy import stats

print("Welcome to numpy Sadman")

array = [12,23,121,34,33,56,7,89,54,33,45,11,34,5,55,67,7,8,9,99,77,21,123,456]
print(f"Median : ${np.median(array)}")
print(f"Mean : ${np.mean(array)}")
most = stats.mode(array)
print(f"Number that appears the most : ${most}")

print(f"Spread Value : ${np.std(array)}")

# spread value means how much the values are spread from each other
# variation is the square of the spread value
# avg number of the spread values

print(f"Variation of Array : ${np.var(array)}")
# standard deviation is the square root of the variation value
print(f"Standard Deviation : ${np.std(array)}")
# standard deviation = Spread Value