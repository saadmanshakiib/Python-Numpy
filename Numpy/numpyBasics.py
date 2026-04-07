import numpy as np

a1 = np.array([1,2,3])
a2 = np.array([2,35,51])

a3 = np.concatenate((a1, a2))
print(a3)
print(f"Data type of the array a3 : {a3.dtype}")

a4 = np.array(['sadman','sakib'])
print(f"Data Type of a4: {a4.dtype}")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

a5 = np.array([2,35,51,21,34,67,891,223])
search = np.where(a5 == 21) # returns index
print(search)

a6 = np.array([2,35,51,21,34,67,891,223,1,122,4556,31313,3465774,1211])
print(f"Sorted Array : {np.sort(a6)}")

arr2 = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr2))