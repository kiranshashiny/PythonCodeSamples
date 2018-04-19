import numpy as np

import matplotlib.pyplot as plt


x = np.arange(1,11) 
y = [ 4,4,6,7,8,9,10,11,12,13]
print ("x = ", x, " y =", y )
plt.title("Matplotlib demo") 
plt.xlabel("x caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y, "or") 
plt.show()
