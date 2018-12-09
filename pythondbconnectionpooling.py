import pyodbc
print(pyodbc.pooling)

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-322F0HM\SA1;'
                      'Database=testdb;'
                      'Trusted_Connection=yes;')
cur= cnxn.cursor()
query='select * from Person'
cur.execute(query)
print(cur.fetchall())

insertquery="INSERT INTO Person(NAME,AGE,CITY)VALUES('{}','{}','{}')"

content= [['vishal',30,'Mumbai'],
          ['ravi',25,'Patna']]

for row in content:
    cur.execute(insertquery.format(*row))
cnxn.commit()


cur.close()
cnxn.close()