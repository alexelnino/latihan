# engine to connect to SQL
# py -m pip isntall sqlalchemy pymysql
import pandas as pd 
import sqlalchemy

mydb = sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://RiantoWibisono:Rianto12345@localhost:3306/fauna'          
)

query = 'select * from aves'
df = pd.read_sql(query, mydb)
print(df)