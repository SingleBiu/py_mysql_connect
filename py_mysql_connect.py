import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "REPLACE YOUR OWN PASSWORD",
    database = "REPLACE YOUR OWN DATABASE"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table1;")

result = mycursor.fetchall()

for row in result:
    print(row)
    
mycursor.close()

mydb.close()