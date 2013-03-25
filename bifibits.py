#vim
import sqlite3
from flask import Flask, request, g, redirect, url_for, abort, \
    render_template, flash

#configuration
DATABASE    = 'bifi.db'
DEBUG       = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def index():
	cur = g.db.execute('select id, name, status, lastupdate from torrents order by id')
	torrents = [dict(id=row[0], name=row[1], status=row[2], lastupdate=row[3]) for row in cur.fetchall()]
	return render_template('index.html', torrents=torrents)

if __name__ == '__main__':
    app.run()