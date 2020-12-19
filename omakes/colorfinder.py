from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
import pickle

X = pd.read_csv('colors.csv', usecols=['R','G','B'])
Y_in=pd.read_csv('colors.csv', usecols=['name'])
Y_o=Y_in.copy()
le = preprocessing.LabelEncoder()
for column_name in Y_in.columns:
  if Y_in[column_name].dtype == object:
    Y_in[column_name] = le.fit_transform(Y_in[column_name])
  else:
    pass
bnb =  GaussianNB()
bnb.fit(X, Y_in.values.ravel())

filename = 'color_model.sav'
pickle.dump(bnb, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
