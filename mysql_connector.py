import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="root", passwd= "Khushi123#", database = "telusko")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()

#either we can use this or use result
# for i in mycursor:
#     print(i)

for i in result:
    print(i)

