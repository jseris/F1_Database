import csv

def MellonArray():
    fpath = r"C:\Users\joeye\Desktop\Projets\Programming\MySQL\MySQLMellon.txt"
    acarray = [] #Container for username and password

    with open(fpath, "r") as ftext:
        reader = csv.reader(ftext)

        for row in reader:
            acarray.append(row) #inserts username and password, respectively, in list

    return acarray
