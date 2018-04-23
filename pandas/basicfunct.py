import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(3))
print ( s )
print ("axes ", s.axes )
print ("dtype ", s.dtype )
print ("empty ", s.empty )
print ("dimension ", s.ndim )
print ("size ", s.size )
print ("values ", s.values )
print ("head ", s.head )
print ("tail ", s.tail )


#axes
#axes	This call returns a data list 
#dtype	This call shows the data type of the Pandas Object.
#empty	indicates if the list is empty or not.
#ndim	returns the dimensions of data, Is it 1 dimension , 2 or 3 - default is 1.
#size	Returns the number of elements 
#values	converts the series to a Numpy ndarray.
#head()	Returns the first element.
#tail()	Returns the last element. Option is there to show the 'n' number of objects.
