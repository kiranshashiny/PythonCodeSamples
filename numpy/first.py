import numpy as np 
a = np.array([1,2,3]) 
print (a )

# Print the digits from start to end-1
a = np.arange ( 1, 100)
print (a )


# Notice the 2 square brackets indicating it is an array !
a = np.array ( [ [ 1,2], [3,4] ] )
print (a )

# print the 2 X 2 d array

a = np.array ([ [ 1,2], [3,4] ], ndmin=2 )
print (a )
print ( " print the 2 X 2 d array as ndmin=3")

a = np.array ([ [ 1,2], [3,4] ], ndmin=3 )
print (a )

print ( " print the 2 X 2 d array as type complex, real + imaginary numbers")

a = np.array ([ [ 1,2], [3,4], [5,6] ], dtype=complex)
print (a )


arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]], dtype = int)
print ( arr ) 

temp= arr[:2]

print ( temp)
temp= arr[::2]

print ( temp)

# add, subtract, and other operations.
a = np.array([1, 2, 3,4])
print ( a)
#print ( a+1)

# Transpose
print ( a.T)


a = np.array( [ [1,2,3],[4,5,6] ] )
print (a)
print (a.T)


print ( a.min())
print ( a.sum())


a = np.array ( [ [4,5,6], [ 1,2,3]] )
b = np.array ( [ [1,2,3], [4,5,6]] )

print ( a+ b )
print ( a* b )
print( "Sorting data ")
print ( np.sort(a )
print ( np.sort(a, axis = None) )
