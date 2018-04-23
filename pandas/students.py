import pandas as pd
import numpy as np

students  = {'name': ['Jane', 'Joe', 'John', 'James', 'Jacob'], 'talent': [25, 19, 79, 9, 20],
        'points': [1, 3, 2, 3, 2],
        'qualify': ['yes', 'no', 'yes', 'no', 'no']}
labels = ['v','w', 'x', 'y', 'z']

df = pd.DataFrame(students , index=labels)
print(df)
