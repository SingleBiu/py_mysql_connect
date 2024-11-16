'''
Author: SingleBiu
Date: 2024-11-14 20:10:36
LastEditors: SingleBiu
LastEditTime: 2024-11-16 22:18:47
Description: A Python drive for MySQL connect.
'''
import pymysql

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    #REPLACE YOU OWN PASSWORD
    password = "PASSWORD",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# VIEW TABLE STRUCTURE
mycursor.execute("desc customers;")
result = mycursor.fetchall()
print("####################")
for row in result:
    print(row)
print("####################")

# TRUNCATE TABLE
mycursor.execute("TRUNCATE TABLE customers")

# INSERT
sql = "INSERT INTO customers(name) VALUES('Zhang San');"
mycursor.execute(sql)
mydb.commit()
sql = "INSERT INTO customers(name) VALUES('Li Si');"
mycursor.execute(sql)
mydb.commit()
sql = "INSERT INTO customers(name) VALUES('Wang Wu');"
mycursor.execute(sql)
mydb.commit()

# SELECT
sql = "SELECT * FROM customers;"
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    print(row)

# UPDATE
sql = "UPDATE customers SET name = 'Zheng San Feng' WHERE name = 'Zhang San'"
mycursor.execute(sql)
mydb.commit()

# CHECK IF IS UPDATE
print("####################")
sql = "SELECT * FROM customers;"
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    print(row)

# DELETE
sql = "DELETE FROM customers WHERE name = 'Zheng San Feng'"
mycursor.execute(sql)
mydb.commit()
print("####################")
print(mycursor.rowcount, "record(s) deleted")

# CHECK IF IS UPDATE
print("####################")
sql = "SELECT * FROM customers;"
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    print(row)
print("####################")
    
mycursor.close()

mydb.close()