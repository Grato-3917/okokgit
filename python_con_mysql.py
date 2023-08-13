import mysql.connector
mydb = mysql.connector.connect(host='localhost',username='root',password='Chinu@2004',database='statuscode0')
mycursor=mydb.cursor()
sql = "INSERT INTO statuscode0 (username, password) VALUES (%s, %s)"
val = ("John", "12345678")
mycursor.execute(sql, val)

mydb.commit()

#print(mycursor.rowcount, "record inserted.")
sql = "SELECT * FROM statuscode0 WHERE username ='John'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
