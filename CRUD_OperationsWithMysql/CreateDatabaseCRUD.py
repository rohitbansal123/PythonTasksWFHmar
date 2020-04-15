
#TODO: comments similar to that of ../ArgparseInputFileProcessing.py
import mysql.connector #Importing Connector package
mysqldb=mysql.connector.connect(host="localhost",user="root",passwd="password")#established connection
mycursor=mysqldb.cursor()#cursor() method create a cursor object
mycursor.execute("create database dbcrud")#Execute SQL Query to create a database
mysqldb.close()#Connection Close
