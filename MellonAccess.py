import csv
import os.path
import mysql.connector

def MellonArray():
    file_name = "MySQLMellon.txt"
    fpath = os.path.abspath(file_name)
    acarray = [] #Container for username and password

    with open(fpath, "r") as ftext:
        reader = csv.reader(ftext)

        for row in reader:
            acarray.append(row) #inserts username and password, respectively, in list
    return acarray

class Creds:
    mc = MellonArray() #Pulls username and password to access MySQL
    def __init__(mcu,mcp,mch)
        mcu = str(mc[0])[2:-2] #Changes the username list object to a string and removes [""]
        mcp = str(mc[1])[2:-2] #Changes the password list object to a string and removes [""]
        mch = str(mc[2])[2:-2] #Changes the host list object to a string and removes [""]

    def crt_crsr():
        cntpass = Creds()
        cnt = mysql.connector.connect(
            user= cntpass.mcu,
            password= cntpass.mcp,
            host= cntpass.mch
            )

        mycursor = cnt.cursor()
        return mycursor
