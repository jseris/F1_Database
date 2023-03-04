import mysql.connector
from MellonAccess import Creds

axes = Creds()

cnt = mysql.connector.connect(
    user= axes.mcu,
    password= axes.mcp,
    host= axes.mch
    )

mycursor = cnt.cursor()

mycursor.execute("CREATE DATABASE F1")

mycursor.execute("SHOW DATABASES")
for databases in mycursor:
    print(databases)

cnt.close()
