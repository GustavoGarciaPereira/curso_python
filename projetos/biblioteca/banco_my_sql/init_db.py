import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="senacrs")

print(mydb)