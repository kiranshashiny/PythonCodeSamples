import pandas as pd
data = [['John',10, 10],['Joe',12, 12],['Jane',13, 12]]
df = pd.DataFrame(data,columns=['Name','Age', 'Weight'],dtype=float)
df2 = pd.DataFrame(data)
print ("Printing Data Frame 1")
print (df )

print ("Printing Data Frame 2")
print (df2 )
