from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)


@app.route('/ttf')
def db():
	try:
		conn = sqlite3.connect('/home/pi/TTFProject/flaskdb/venv/TTF.db')
		c = conn.cursor()
		data = c.execute('SELECT * FROM weather;')
		clean = data.fetchall()
		return(render_template(index.html, weather=clean))
		conn.close()
	except Exception, e:
		return str(e)

def db2():
		try:
		conn = sqlite3.connect('/home/pi/TTFProject/flaskdb/venv/TTF.db')
		c = conn.cursor()
		data = c.execute('SELECT * FROM userData;')
		clean = data.fetchall()
		return(render_template(index.html, info=clean))
		conn.close()
	except Exception, e:
		return str(e)

if __name__ == "__main__":
	app.run()

