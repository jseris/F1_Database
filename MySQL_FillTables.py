import pandas as pd
import numpy as np
import sqlalchemy
import mysql.connector
from os import listdir
from os.path import isfile, join, abspath
from MellonAccess import MellonArray

f1folder = "F1Data_archive"
dataloc = abspath(f1folder) #Where all the F1 data resides
f1files = [f for f in listdir(dataloc) if isfile(join(dataloc, f))]  #Gathering data files names.

mc = MellonArray() #Pulls username and password to access MySQL.
mcu = str(mc[0])[2:-2] #Cleaning string username for SQL connector.
mcp = str(mc[1])[2:-2] #Cleaning string password for SQL connector.
mch = str(mc[2])[2:-2] #Changes the host list object to a string and removes [""]
engine = sqlalchemy.create_engine("mysql://" + mcu + ":" + mcp + "@localhost/F1") #to_sql function requires a sqlalchemy engine. Unable to use mysql connector.
n = 0

#MySQL Connector.
cnt = mysql.connector.connect(
    user= mcu,
    password= mcp,
    host= mch
    )
mycursor = cnt.cursor()

# Pull table names from MySQL into a cleaned list.
mycursor.execute("USE F1")
mycursor.execute("SHOW tables")
dbtables = mycursor.fetchall()
dbclean = [x[0] for x in dbtables] # Fetchall function pulls in a list of tuples. Added line to make into cleaned strings for to_sql function.

# Moving data from CSVs into MySQL.
for f in f1files:
    test = pd.read_csv(join(dataloc,f1files[n]),delimiter=",")
    test = test.where(test != "\\N",np.nan) # Replacing null values in CSVs with NaN. to_sql function does not accept /N as null.
    test.to_sql(dbclean[n],con=engine,if_exists="append",index=False)
    n = n + 1
