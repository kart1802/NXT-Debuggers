import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="apte@mysql!",
  database="demo"
)


mycursor = mydb.cursor()

mycursor.execute("UPDATE datainfo SET number=0,value=0")

mydb.commit()

