from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)


@app.route('/ttf')
def db():
	conn = sqlite3.connect('/home/pi/TTFProject/flaskdb/venv/TTF.db')
	c = conn.cursor()
#	countRows = c.rowcount
	data = c.execute('SELECT * FROM weather;')
#	for row in data:
	clean = data.fetchall()
	return(render_template('index.html', item=clean))
#	return(clean)
if __name__ == "__main__":
	app.run()

