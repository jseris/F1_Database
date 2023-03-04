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
    def __init__(self):
        self.mc = MellonArray()
        self.mcu = str(self.mc[0])[2:-2] #Changes the username list object to a string and removes [""]
        self.mcp = str(self.mc[1])[2:-2] #Changes the password list object to a string and removes [""]
        self.mch = str(self.mc[2])[2:-2] #Changes the host list object to a string and removes [""]
