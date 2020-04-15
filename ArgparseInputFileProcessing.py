
# TODO: use shebang statement

import mysql.connector
import csv
import argparse

# TODO: separate functions for different tasks

# TODO: separate function to handle connection creation - can return connection/cursor
# TODO: Whatif the argument parsing fails, how will you close the connection
# TODO: there is a large gap between a resource acquisition(database connection) and its usage
# try to keep resource acquistion and its usage as close as possible
conn = mysql.connector.connect(host="localhost",user="root",passwd="password",database="crud")#established connection between your database
mycursor=conn.cursor()#cursor() method create a cursor object


# TODO: separate function parse_args() - should return the parsed arguments
parser = argparse.ArgumentParser(description= "input CSV values from txt and load these in a table ")
parser.add_argument("input", help = "Input File")

args = parser.parse_args()

print('inputfile:', args.input)

# TODO: use better naming 
ain = args.input
print(ain)
# new things added for csv to mysql table loading of data
csv_file = open(ain)
csv_data = csv.reader(csv_file)
# execute and insert the csv into the database.
for row in csv_data:
	mycursor.execute('INSERT INTO employee(id,name,dept,salary)''VALUES(%s, %s, %s, %s)',row)
	#print (row)
    #print(row['id'], row['name'], row['dept'],row['salary'])
#close the connection to the database.
conn.commit()
mycursor.close()
print ("CSV records has been loaded into the database crud in employee table")



