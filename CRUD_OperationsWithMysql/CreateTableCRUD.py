#Create a table into dbcrud database
import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="password",database="dbcrud")#established connection between your database
mycursor=mysqldb.cursor()#cursor() method create a cursor object
mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)")#Execute SQL Query to create a table into your database
mysqldb.close()#Connection Close