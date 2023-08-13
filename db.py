import mysql.connector
mydb = mysql.connector.connect(host='localhost',username='root',password='Chinu@2004',database='sc0')

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE info (name VARCHAR(255), password VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor=mydb.cursor()


mycursor.execute(sql, val)
mycursor.execute("SHOW TABLES")
mydb.commit()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


