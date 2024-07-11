import mysql.connector 


dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='AJ2K26@Raj',
)
#prepare a cursor object
cursorObject=dataBase.cursor()
#create a datbase
cursorObject.execute("CREATE Projectdb")
print("All DOne")
