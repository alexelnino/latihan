import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# trying new data
# df = [
#     {'id': 1, 'kota': 'Jakarta', 'jumlah': 45},
#     {'id': 1, 'kota': 'Bandung', 'jumlah': 66},
#     {'id': 2, 'kota': 'Jakarta', 'jumlah': 34},
#     {'id': 2, 'kota': 'Bandung', 'jumlah': 76},
#     {'id': 3, 'kota': 'Jakarta', 'jumlah': 99},
#     {'id': 3, 'kota': 'Bandung', 'jumlah': 12},
# ]
df = [
    {'id': 1, 'kota': 'Jakarta', 'jumlah': 45, 'nilai': 90},
    {'id': 1, 'kota': 'Bandung', 'jumlah': 66, 'nilai': 92},
    {'id': 2, 'kota': 'Jakarta', 'jumlah': 34, 'nilai': 67},
    {'id': 2, 'kota': 'Bandung', 'jumlah': 76, 'nilai': 78},
    {'id': 3, 'kota': 'Jakarta', 'jumlah': 99, 'nilai': 88},
    {'id': 3, 'kota': 'Bandung', 'jumlah': 12, 'nilai': 98},
]

# # data pivotting
# df = pd.DataFrame(df)
# print(df)
# print(df.pivot(index = 'id', columns = 'kota'))         # this is suitable for data distribution
# # if want to check only 'jumlah' data
# print(df.pivot(index = 'id', columns = 'kota')['jumlah']) 

# another writing method
df = pd.DataFrame(df)
df = df.pivot(index = 'id', columns = 'kota')['jumlah']    
print(df)

df2 = pd.melt(df, id_vars=['id'])
print(df2)