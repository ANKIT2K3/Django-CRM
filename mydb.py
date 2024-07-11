import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='AJ2K26@Raj',
    database='projectdb'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()
print(result)
connection.close()
