import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv(
    'tlkm.csv',
    index_col = False,
    parse_dates = ['Tanggal']    
)

# # checking type of tanggal column
# print(df.head(1))
# print(type(df['Tanggal'][0]))

# print the first 5 data
df = df.head()
df = df[['Tanggal', 'Open', 'Close']]
# print(df)

# pivotting
print(df.pivot(
    index = 'Tanggal',
    columns = 'Open'
))          # fails, the data doesn't match