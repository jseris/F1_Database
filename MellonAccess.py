import csv
import os.path

def MellonArray():
    file_name = "MySQLMellon.txt"
    fpath = os.path.abspath(file_name)
    acarray = [] #Container for username and password

    with open(fpath, "r") as ftext:
        reader = csv.reader(ftext)

        for row in reader:
            acarray.append(row) #inserts username and password, respectively, in list

    return acarray

MellonArray()
