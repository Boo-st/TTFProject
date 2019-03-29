import Read
import dht11
import sqlite3
import datetime
	
def sensorRead():
	ID = Read.machinedata()
	weather = dht11.thermo()
	return(ID, weather)

def dbConnect(dbFile):
	try:
		conn = sqlite3.connect(dbFile)
		return(conn)
	except error as E:
		print(E)
	return(None)

def createTable(conn, sqlStatement):
	try:
		c = conn.cursor()
		c.execute(sqlStatement)
	except error as E:
		print(E)

#def insertData(conn, sqlStatement, ):
#	try:
#		c = conn.cursor()
#		c.execute(sqlStatement)
#	except error as E:
#		print(E)

def main():
	datetime = datetime.datetime.now()
	ID = sensorRead[0]
	temperature = sensorRead[1]
	humidity = sensorRead[2]

	database = ("/home/pi/TTFProject/flaskdb/venv/TTF.db")

	sql_create_user = (""" CREATE TABLE IF NOT EXISTS userData (
                                        id integer PRIMARY KEY,
                                        datetime integer
                                    ); """)

	sql_create_weather = (""" CREATE TABLE IF NOT EXISTS weather (
                                        temperature integer PRIMARY KEY,
                                        humidity integer NOT NULL,
                                    ); """)

	sql_insert_userData = ("INSERT INTO userData (id, DATETIME) VALUES (?, ?)")
	sql_insert_weather = ("INSERT INTO weather (temperature, humidity) VALUES (?, ?)")


	conn = dbConnect(database)
	if conn is not None:
		c = conn.cursor()
		c.execute(sql_insert_userData, [ID, datetime])
		c.execute(sql_insert_weather, [temperature, humidity])
		conn.commit()
		conn.close()

if __name__ == '__main__':	
	main()




