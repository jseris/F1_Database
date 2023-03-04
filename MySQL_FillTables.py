import pandas as pd
import numpy as np
import sqlalchemy
import mysql.connector
from os import listdir
from os.path import isfile, join, abspath
from MellonAccess import Creds

axes = Creds()
f1folder = "F1Data_archive"
dataloc = abspath(f1folder) #Where all the F1 data resides
f1files = [f for f in listdir(dataloc) if isfile(join(dataloc, f))]  #Gathering data files names.

engine = sqlalchemy.create_engine("mysql://" + axes.mcu + ":" + axes.mcp + "@localhost/F1") #to_sql function requires a sqlalchemy engine. Unable to use mysql connector.
n = 0

cnt = mysql.connector.connect(
    user= axes.mcu,
    password= axes.mcp,
    host= axes.mch
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
