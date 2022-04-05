import mysql.connector as a
# import MySOL.Connector as a
from sqlite3 import Cursor
from tokenize import Number



con = a.connect(host="localhost",user="root",password="",database="deepak")

Cursor =con.cursor()

number= int(input("Enter Your Number"))
name = input("Enter Your Name")
age = int(input("Enter Your Age"))
gender = input("Enter Your Gender")
city = input("Enter Your")

query ="insert into info values({},'{}',{},'{}','{}')".format(number,name,age,gender,city)

Cursor.execute(query)
con.commit()
print("Data Intrted")

