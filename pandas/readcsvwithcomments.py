import pandas as pd

df = pd.read_csv('HON.csv')
#This prints everything to everything.


# This reads in the column names as well, and assigns the column names
df = pd.read_csv('HON.csv', names=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume' ], comment='#')

#This prints as a Series in Pandas. one after another 
print ( df['Date'])

# This prints as a numpy array.  All in one line.
print ( df['Date'].values )

print ("Printing the Open now " )
print ( df['Open'].values )

