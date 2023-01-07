import mysql.connector
from MellonAccess import MellonArray

mc = MellonArray() #Pulls username and password to access MySQL
mcu = str(mc[0])[2:-2] #Changes the username list object to a string and removes [""]
mcp = str(mc[1])[2:-2] #Changes the password list object to a string and removes [""]

cnt = mysql.connector.connect(
    user= mcu,
    password= mcp,
    host= "127.0.0.1"
    )

mycursor = cnt.cursor()

mycursor.execute("CREATE DATABASE F1")

mycursor.execute("SHOW DATABASES") #Lists all the databases in MySQL
for databases in mycursor:
    print(databases)

cnt.close()
