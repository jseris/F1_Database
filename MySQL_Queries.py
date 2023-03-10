from MellonAccess import MellonArray
import mysql.connector
import pandas as pd

mc = MellonArray() #Pulls username and password to access MySQL.
mcu = str(mc[0])[2:-2] #Cleaning string username for SQL connector.
mcp = str(mc[1])[2:-2] #Cleaning string password for SQL connector.
mch = str(mc[2])[2:-2] #Cleaning string host for SQL connector.

#MySQL Connector.
cnt = mysql.connector.connect(
    user= mcu,
    password= mcp,
    host= mch
    )
mycursor = cnt.cursor()

mycursor.execute("USE F1")

def driverstat(): #driver data by race. Breaking up SQL statement by variables to promote easier reading.
    fields = "d.forename, d.surname, r.name, r.date, ds.position, ds.points"
    table = "driverstandings ds"
    join1 = "drivers d ON d.driverId = ds.driverId"
    join2 = "races r ON r.raceId = ds.raceId"
    order = "date DESC, position"
    script = f"""SELECT {fields} FROM {table}
                    INNER JOIN {join1}
                    INNER JOIN {join2}
                    ORDER BY {order};
                    """
    #run = mycursor.execute(script)
    df = pd.read_sql(script, cnt) # There is a warning using a connector other than SQLAlchemy. Output still looks good :)
    print(df)

def ferraristat(): #Ferrari constructor points data for each race. Breaking up SQL statment by variables to promote easier reading.
    fields = "c.name, cr.points, r.name, r.date, r.year"
    table = "constructorresults cr"
    join1 = "constructor c ON c.constructorId = cr.constructorId"
    join2 = "races r ON r.raceId = cr.raceId"
    wh = "c.name = 'Ferrari'"
    script = f"""SELECT {fields} FROM {table}
                    INNER JOIN {join1}
                    INNER JOIN {join2}
                    WHERE {wh};
                    """
    df = pd.read_sql(script, cnt) # There is a warning using a connector other than SQLAlchemy. Output still looks good :)
    print(df)

driverstat()
ferraristat()
