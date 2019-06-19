import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = [
    {'id': 1, 'Jakarta': 45, 'Bandung': 90},
    {'id': 2, 'Jakarta': 66, 'Bandung': 92},
    {'id': 3, 'Jakarta': 34, 'Bandung': 67},
    {'id': 4, 'Jakarta': 76, 'Bandung': 78},
    {'id': 5, 'Jakarta': 99, 'Bandung': 88},
    {'id': 6, 'Jakarta': 12, 'Bandung': 98},
]

df = pd.DataFrame(df)
df = pd.melt(
    df, 
    id_vars=['id'], 
    var_name='city', 
    value_name='polusi'
)
print(df)

# cross tab --> to calculate the frequency of each value grouped by variable (city name)
# dfCrosstab = pd.crosstab(df['city'], df['polusi'])
dfCrosstab = pd.crosstab(
    df['city'],
    df['polusi'],
    values=df['polusi'],
    # aggfunc='mean',
    aggfunc='sum'
)
print(dfCrosstab)
