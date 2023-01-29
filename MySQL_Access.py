import mysql.connector
from MellonAccess import MellonArray

mc = MellonArray() #Pulls username and password to access MySQL
mcu = str(mc[0])[2:-2] #Changes the username list object to a string and removes [""]
mcp = str(mc[1])[2:-2] #Changes the password list object to a string and removes [""]
mch = str(mc[2])[2:-2] #Changes the host list object to a string and removes [""]

cnt = mysql.connector.connect(
    user= mcu,
    password= mcp,
    host= mch
    )

mycursor = cnt.cursor()

print("Success!")


mycursor.close()
