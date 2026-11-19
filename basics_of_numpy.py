# 19-11-2026
# numpy
# it is python lib. used for fast mathematical operations

import numpy as np #python lib

list= [1,2,5,3,6]
print(list)
print(type(list))

#creating array
# arrays are my rows only
# create 1 d array
array1d = np.array([1,2,3,4,5])
print(array1d)
print(type(array1d))

# checking shape of array
array1d.ndim
# 1 dimension
#shape of array
array1d.shape

# 2d array
# when we combine multiple 1d array together will get 2d array
array2d=np.array([[1,5,2,3],[8,8,9,2]])
array2d
array2d.ndim  #dimension of array
array2d.shape # shape # (rows, columns)  # 2 rows and 4 columns


# create 2d array of shape 2,3    # no of elements should be same
array2d=np.array([[1,5,2],[8,9,2]])
array2d

# creating 3d array
# when we combine multiple 2d array, we'll get 3d array
array3d = np.array([[[1,5,2,3],[8,8,9,2]],[[1,5,2,3],[8,18,9,2]]])
array3d
# shape (blocks,rows,columns)
array3d.shape

# create a 3d array of 3,2,2
array3d = np.array([[[2,3],[9,2]],[[2,3],[9,2]],[[2,3],[9,2]]])
array3d


# Arithmatic operation on array
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print("sum of array:",a+b)
print("Substraction of array:",a-b)
print("Multiplication of array:",a*b)
print("Division of array:",a/b)

# scaler
# scaler is my single values used to scale up and down the elememts in a particular array
array1d=np.array([5,6,7,8])
#increase the value of each element in the array by 5
var = array1d+5   # 5 is my scaler value.
var

array1d=np.array([5,6,7,8])
a=np.array([5,5,5,5])    # broadcasting
array1d+a

# indexing
array1d=np.array([1,2,5,6,8])
print(array1d)
print(array1d[3])
print(array1d[-4])


# indexing in 2d array
array2d=np.array([[1,2,5,6,8],[51,29,52,62,87]])
print(array2d)


# access 62 from the array
print(array2d[1,3])
#access 8 from the array
print (array2d[0,4])


# indexing in 3d array
array3d=np.array([[[1,2,3],[18,82,33]],[[81,221,387],[951,782,30]]])
print(array3d)
# access 387 from the array
print(array3d[1,0,2])
# access 782
print(array3d[1,1,1])