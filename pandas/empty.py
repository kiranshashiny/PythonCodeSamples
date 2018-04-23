import pandas as pd
import numpy as np

#s = pd.Series([0,3,4])
#print (s)

s = pd.Series([1,2,3], dtype=int)
#print (s)

print ( s.values )
#
#print ("data frame")
df = pd.DataFrame([1,2,3,4], dtype=int)
print (df)
print ( df.values )

df = {'Qtr1' : pd.Series( ['J','F', 'Ma'], index=[1,2,3] ),
      'Qtr2' : pd.Series(['Ap', 'May', 'Jun'], index=[1,2,3])} 

df = {'Qtr1' : pd.Series( ['J','F', 'Ma'], index=['a','b','c'] )}
df = {'Qtr1' : pd.Series( ['J','F', 'Ma'], index=[1,2,3] )}


#data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
#df = pd.DataFrame(data, dtype=int)
#print (df)



#s = pd.Series(["john", "joe", "sam"] )
#print (s)
#print ("EMpty data frame ");
#df = pd.DataFrame ( )
#print (df)
#print (" hello world");
#df = pd.DataFrame ([1,2,3,4,5] )
#print (df)
#print (" hello world");
#
#data =  [['John','M'],['Jane','F'],['Sam','M']]
#df = pd.DataFrame(data,columns=['Name','Sex'])
#print ( df )


