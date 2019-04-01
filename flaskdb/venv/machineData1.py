import Read
import dht11
import sqlite3
import datetime

# def getSensor():
# 	tmpIn, humIn = dht11.getData()
# 	return(tmpIn, humIn)	

def getID():
	ID = Read.machinedata()
	return(ID)

def dbConnect(dbFile):
	try:
		conn = sqlite3.connect(dbFile)
		return(conn)
	except Error as E:
		print(E)
	return(None)

def createTable(conn, sqlStatement):
	c = conn.cursor()
	c.execute(sqlStatement)
	# except Error as E:
	# 	print(E)

def insertData(conn, sqlStatement):
	try:
		c = conn.cursor()
		c.execute(sqlStatement)
	except Error as E:
		print(E)

def main():
	dateTime = datetime.datetime.now()
	ID = getID()
	temperature, humidity = dht11.getData()

	database = ("/home/pi/TTFProject/flaskdb/venv/TTF.db")

	sql_create_user = """ CREATE TABLE IF NOT EXISTS userData (
                                        id integer PRIMARY KEY,
                                        datetime integer
                                    ); """

	sql_create_weather = """ CREATE TABLE IF NOT EXISTS weather (
                                        temperature integer PRIMARY KEY,
                                        humidity integer NOT NULL
                                    ); """

	sql_insert_userData = ("INSERT INTO userData (id, DATETIME) VALUES (?, ?)")
	sql_insert_weather = ("INSERT INTO weather (temperature, humidity) VALUES (?, ?)")


	conn = dbConnect(database)
	if conn is not None:
		# createTable(conn, sql_create_user)
		# createTable(conn, sql_create_weather)
		# insertData(conn, sql_insert_userData, [ID, dateTime])
		# insertData(conn, sql_insert_weather, [temperature, humidity])
		c = conn.cursor()
		c.execute(sql_insert_userData, [ID, dateTime])
		c.execute(sql_insert_weather, [temperature, humidity])
		conn.commit()
		conn.close()

if __name__ == '__main__':	
	main()




