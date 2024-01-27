import numpy as np

# # Creating Arrays:

# # 1D array
arr_1d = np.array([1, 2, 3])
# arr_1d = np.array([1, 2, 3],dtype="int16") #2 bytes
# print("1D Array:")
# print(arr_1d)
# print(type(arr_1d[0]))
# arr_1d = arr_1d.astype(np.int32)
# print(arr_1d)
# print(type(arr_1d[0]))
# data_type = arr_1d.dtype
# print("Data type:", data_type)

# # 2D array
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("\n2D Array:")
# print(arr_2d)
# print(arr_2d[0][2])

# # Array with zeros
# zeros_arr = np.zeros((3, 4),dtype="int32")
# print("\nArray with Zeros:")
# print(zeros_arr)

# # # Array with ones
# ones_arr = np.ones((2, 3),dtype="int16")
# print("\nArray with Ones:")
# print(ones_arr)

# # Array with a range of values
# range_arr = np.arange(0, 10, 2)
# print("\nArray with a Range:")
# print(range_arr)

# # Basic Operations:

# # Addition

# result_add = arr_1d + arr_1d
# print("\nAddition Result:")
# print(result_add)

# # Multiplication
# result_mul = arr_1d * 2
# print("\nMultiplication Result:")
# print(result_mul)

# # Element-wise square root
# result_sqrt = np.sqrt(arr_1d)
# print("\nSquare Root Result:")
# print(result_sqrt)

# # Indexing and Slicing:

# # Accessing element
# element = arr_1d[0]
# print("\nAccessing Element:")
# print(element)

# # Slicing
# subarray = arr_1d[1:3]
# print("\nSliced Subarray:")
# print(subarray)

# # Mathematical Functions:

# # Sum of all elements
total_sum = np.sum(arr_1d)
print("\nSum of Elements:")
print(total_sum)

# # Mean of elements
mean_value = np.mean(arr_1d)
print("\nMean of Elements:")
print(mean_value)

# # Element-wise exponentiation
exp_arr = np.exp(arr_1d)
print("\nExponential of Elements:")
print(exp_arr)


""" The NumPy library contains multidimensional array and matrix data structures 
(you’ll find more information about this in later sections). It provides ndarray,
a homogeneous n-dimensional array object, with methods to efficiently operate on it.
NumPy can be used to perform a wide variety of mathematical operations on arrays.
It adds powerful data structures to Python that guarantee efficient calculations with arrays
and matrices and it supplies an enormous library of high-level mathematical functions that
operate on these arrays and matrices.
"""
