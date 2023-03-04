import mysql.connector
from MellonAccess import Creds

axes = Creds()

cnt = mysql.connector.connect(
    user= axes.mcu,
    password= axes.mcp,
    host= axes.mch
    )

mycursor = cnt.cursor()

mycursor.execute("USE F1")

mycursor.execute("CREATE TABLE Circuits(circuitId INT PRIMARY KEY, circuitRef VARCHAR(50), name VARCHAR(50), location VARCHAR(50), country VARCHAR(50), lat VARCHAR(50), lng VARCHAR(50), alt INT, url VARCHAR(255))")
mycursor.execute("CREATE TABLE Constructor(constructorId INT PRIMARY KEY, constructorRef VARCHAR(50), name VARCHAR(50), nationality VARCHAR(50), url VARCHAR(255))")
mycursor.execute("CREATE TABLE ConstructorResults(constructorResultsId INT PRIMARY KEY, raceId INT, constructorId INT, points INT, status VARCHAR(50))")
mycursor.execute("CREATE TABLE ConstructorStandings(constructorStandingsId INT PRIMARY KEY, raceId INT, constructorId INT, points INT, position INT, positionText VARCHAR(5), wins INT)")
mycursor.execute("CREATE TABLE DriverStandings(driverStandingsId INT PRIMARY KEY, raceId INT, driverId INT, points INT, position INT, positionText VARCHAR(5), wins INT)")
mycursor.execute("CREATE TABLE Drivers(driverId INT PRIMARY KEY, driverRef VARCHAR(50), number INT, code CHAR(3), forename VARCHAR(50), surname VARCHAR(50),dob VARCHAR(10), nationality VARCHAR(50), url VARCHAR(255))")
mycursor.execute("CREATE TABLE Lap_Times(raceId INT, driverId INT, lap INT, position INT, time VARCHAR(15), milliseconds VARCHAR(7))")
mycursor.execute("CREATE TABLE Pit_Stops(raceId INT, driverId INT, stop INT, lap INT, time VARCHAR(15), duration VARCHAR(15), milliseconds VARCHAR(7))")
mycursor.execute("CREATE TABLE Qualifying(qualifyId INT PRIMARY KEY, raceId INT, driverID INT, constructorId INT, number INT, position INT, q1 VARCHAR(10), q2 VARCHAR(10), q3 VARCHAR(10))")
mycursor.execute("CREATE TABLE Races(raceId INT PRIMARY KEY, year INT, round INT, circuitId INT, name VARCHAR(50), date DATE, time VARCHAR(8), url VARCHAR(100), fp1_Date DATE, fp1_Time VARCHAR(10), fp2_Date DATE, fp2_Time VARCHAR(10),fp3_Date DATE, fp3_Time VARCHAR(10),quali_Date DATE, quali_Time VARCHAR(10),sprint_Date DATE, sprint_Time VARCHAR(10))")
mycursor.execute("CREATE TABLE Results(resultId INT, raceId INT, driverId INT, constructorId INT, number INT, grid INT, position INT, positionText VARCHAR(5), positionOrder INT, points INT, laps INT, time VARCHAR(10), milliseconds VARCHAR(10), fastestLap INT, ranking INT, fastestLapTime VARCHAR(15), fastestLapSpeed VARCHAR(10), statusId INT)")
mycursor.execute("CREATE TABLE Seasons(year INT, url VARCHAR(100))")
mycursor.execute("CREATE TABLE Sprint_Results(resultId INT, raceId INT, driverId INT, constructorId INT, number INT, grid INT,position INT, positionText VARCHAR(10), positionOrder INT, points INT, laps INT, time VARCHAR(15), milliseconds VARCHAR(10), fastestLap INT, fastestLapTime VARCHAR(15), statusId INT)")
mycursor.execute("CREATE TABLE Status(statusId INT, status VARCHAR(20))")

mycursor.close()
