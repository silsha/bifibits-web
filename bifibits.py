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
	return render_template('index.html');

if __name__ == '__main__':
    app.run()