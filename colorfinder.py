from sklearn import preprocessing
import numpy as np
import pandas as pd
X = pd.read_csv('colors.csv', usecols=['name','R','G','B'])
print(X)