import numpy as np 

oneD = np.array([1, 2, 3, 4,3,6,3,6,3,6])
twoD = np.array([[1,2, 3], [3, 4, 6]])
threeD = np.array([[[1,3], [3,4]], [[3, 6], [9, 8]]])

# print(oneD.ndim)
# print(twoD.ndim)
# print(threeD.ndim)

#indexing array
print(threeD[1,1,1])

#slicking array 
print(twoD[0:2, 1:2])

print(oneD.dtype)

# copy = oneD.copy()
# copy[0] = 42
# print(oneD)
# print(copy)

# view = oneD.view()
# view[0] = 42
# print(oneD)
# print(view)

print(oneD.shape)

print(twoD.reshape(3,2))