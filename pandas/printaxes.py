import pandas as pd
import numpy as np

# Prints the start, stop and the step of the elements in the array.

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print ("The axes are:")
print (s.axes )

print ( pd.Series(np.arange(5) ) )


