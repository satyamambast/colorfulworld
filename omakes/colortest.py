import pickle
import numpy as np
import pandas as pd
Y_in=pd.read_csv('colors.csv', usecols=['name'])
number_column = Y_in.loc[:,'name']
numbers = number_column.values

filename = 'color_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
while True:
    R=int(input())
    G=int(input())
    B=int(input())
    arry=[[R,G,B]]
    result = loaded_model.predict(arry)
    print(numbers[result[0]])