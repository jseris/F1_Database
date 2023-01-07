import pandas
import mysql.connector
from os import listdir
from os.path import isfile, join
from MellonAccess import MellonArray

dataloc = "C:\\Users\\joeye\\Desktop\\Projets\\Programming\\Data\\F1Data_archive\\" #Directory with all F1 data files
f1files = [f for f in listdir(dataloc) if isfile(join(dataloc, f))]  #runs through files in F1 data directory and joins names as strings to list

mc = MellonArray() #Pulls username and password to access MySQL
mcu = str(mc[0])[2:-2] #Changes the username list object to a string and removes [""]
mcp = str(mc[1])[2:-2] #Changes the password list object to a string and removes [""]

cnt = mysql.connector.connect(
    user= mcu,
    password= mcp,
    host= "127.0.0.1"
    )

mycursor = cnt.cursor()
