import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="apte@mysql!",
  database="demo"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT high,low,close FROM datainfo")
result = mycursor.fetchall()

mylisth=list()
mylistl=list()
mylistc=list()

for x,y,z in result:
    mylisth.append(x)
    mylistl.append(y)
    mylistc.append(z)

i=0
if mylistl[i]>mylistl[i+1] and mylistc[i]>mylistc[i+1]:
    sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
    sql2 = "UPDATE datainfo SET number=%s WHERE srno=%s"
    val1 = ("A",i+1)
    val2 = ("1",i+2)
    mycursor.execute(sql1,val1)
    mycursor.execute(sql2,val2)
    mydb.commit()
    
