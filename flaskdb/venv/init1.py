from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/ttf')
def db():
	conn = sqlite3.connect('/home/pi/TTFProject/flaskdb/venv/TTF.db')
	c = conn.cursor()
	data = c.execute('SELECT * FROM weather')

	clean = data.fetchall()
	data2 = c.execute('SELECT * FROM userData')
	clean2 = data2.fetchall()
	return(render_template('index1.html', weather=clean, userdata=clean2))
	conn.close()

if __name__ == "__main__":
	app.run()

