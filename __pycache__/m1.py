import mysql.connector
mydb=mysql.connector.connect(host='localhost',user ='root',password='Chinu@2004')
a = mydb.cursor()
a.execute("CREATE DATABASE statuscode1")
