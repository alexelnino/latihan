# read SQL database using pandas package
import mysql.connector 
import pandas as pd 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'RiantoWibisono',
    passwd = 'Rianto12345',
    database = 'fauna'
)

query = 'select * from aves'
df = pd.read_sql(query, con = mydb)
print(df)