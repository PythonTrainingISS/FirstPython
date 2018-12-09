import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-322F0HM\SA1;'
                      'Database=testdb;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM testdb..Person')

for row in cursor:
    print(row)

cursor.close()
cnxn.close()
