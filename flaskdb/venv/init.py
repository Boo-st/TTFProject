from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)


@app.route('/ttf')
def db():
	conn = sqlite3.connect('/home/pi/TTFProject/flaskdb/venv/TTF.db')
	c = conn.cursor()
	data = c.execute('SELECT * FROM userData UNION SELECT * FROM weather;')
	clean = str(data.fetchall())
#	return(render_template('index.html', data=data))
	return(clean)
if __name__ == "__main__":
	app.run()

