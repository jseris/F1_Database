import pandas as pd
import sqlalchemy
import mysql.connector
from os import listdir
from os.path import isfile, join
from MellonAccess import MellonArray

dataloc = "C:\\Users\\joeye\\Desktop\\Projets\\Programming\\Data\\F1Data_archive\\" #Directory with all F1 data files
f1files = [f for f in listdir(dataloc) if isfile(join(dataloc, f))]  #Gathering data files names


mc = MellonArray() #Pulls username and password to access MySQL
mcu = str(mc[0])[2:-2] #Cleaning string username for SQL connector
mcp = str(mc[1])[2:-2] #Cleaning string password for SQL connector
engine = sqlalchemy.create_engine("mysql://" + mcu + ":" + mcp + "@localhost/F1") #to_sql function requires a sqlalchemy engine. Unable to use mysql connector.

cnt = mysql.connector.connect(
    user= mcu,
    password= mcp,
    host= "127.0.0.1"
    )

mycursor = cnt.cursor()
