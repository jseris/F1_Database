import mysql.connector
from MellonAccess import Creds

axes = Creds()

cnt = mysql.connector.connect(
    user= axes.mcu,
    password= axes.mcp,
    host= axes.mch
    )

mycursor = cnt.cursor()

print("Success!")


mycursor.close()
