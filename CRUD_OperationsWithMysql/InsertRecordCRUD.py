
#TODO: comments similar to that of ../ArgparseInputFileProcessing.py
import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="dbcrud")#established connection between your database
mycursor=mysqldb.cursor()#cursor() method create a cursor object
try:
   #Execute SQL Query to insert record
   mycursor.execute("insert into student values(1,'ROHIT',100),(2,'Kumar',89),(3,'Sohan',90)")
   mysqldb.commit() # Commit is used for your changes in the database
   print('Record inserted successfully...')
except:
   # rollback used for if any error
   mysqldb.rollback()
mysqldb.close()#Connection Close
