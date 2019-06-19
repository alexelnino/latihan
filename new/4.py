# pip install mysql-connector-python
import mysql.connector 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'RiantoWibisono',
    passwd = 'Rianto12345',
    database = 'fauna'
)

mycursor = mydb.cursor()
mycursor.execute('select * from aves')
hasil = mycursor.fetchall()
print(hasil)        # the result would be lists inside a tuple
