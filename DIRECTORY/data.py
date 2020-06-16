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

total=len(mylistc)
i=0
while i<(total-1) :
    if mylisth[i]<mylisth[i+1] and mylistc[i]<mylistc[i+1] :
        sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
        sql2 = "UPDATE datainfo SET number=%s WHERE srno=%s"
        val1 = ("A",i+1)
        val2 = ("1",i+2)
        mycursor.execute(sql1,val1)
        mycursor.execute(sql2,val2)
        mydb.commit()
        temlow1 = mylistl[i]
        temlow2 = mylistl[i+1]
        m=1+2
        while mylisth[i]>mylisth[m] and mylistc[i]>mylistc[m]:
            m += 1
        
        temlow3 = mylistl[m]
        sql2 = "UPDATE datainfo SET number=%s WHERE srno=%s"
        sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
        val3 = ("2",m+1)
        val4 = ("A",m+1)
        mycursor.execute(sql1,val4)
        mycursor.execute(sql2,val3)
        mydb.commit()
        spl= min(temlow1,temlow2,temlow3)
        if temlow1==spl:
            sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
            val5= ("SPL",i+1)
            mycursor.execute(sql1,val5)
            mydb.commit()
        elif temlow2==spl:
            sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
            val5= ("SPL",i+2)
            mycursor.execute(sql1,val5)
            mydb.commit()
        else:
            sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
            val5= ("SPL",m+1)
            mycursor.execute(sql1,val5)
            mydb.commit()

        n=m



        while mylistl[m]<mylistl[n+1] and mylistc[m]<mylist[n+1]:
            n += 1
        sql2 = "UPDATE datainfo SET number=%s WHERE srno=%s"
        val6=("1",n+2)
        mycursor.execute(sql2,val6)
        mydb.commit()
        while mylistl[m]<mylistl[n+1] and mylistc[m]<mylist[n+1]:
            n += 1
        sql2 = "UPDATE datainfo SET number=%s WHERE srno=%s"
        sql1 = "UPDATE datainfo SET value=%s WHERE srno=%s"
        val8=("A",n+2)
        val7=("2",n+2)
        mycursor.execute(sql2,val7)
        mycursor.execute(sql1,val8)
        mydb.commit()



    else:
        i += 1


        