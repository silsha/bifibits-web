#vim
import sqlite3
from flask import Flask, request, g, redirect, url_for, abort, \
    render_template, flash, session
from wtforms import Form, TextField, validators
from model import QueueEntry
import os
from sqlobject import connectionForURI, sqlhub

#configuration
DATABASE    = 'bifi.db'
DEBUG       = True
SECRET_KEY  = "CHANGEME"

app = Flask(__name__)
app.config.from_object(__name__)

db_filename = os.path.abspath(app.config['DATABASE'])
connection_string = 'sqlite:' + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

class SubmitForm(Form):
    link = TextField('Torrent- or Magnet-URL')

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
    torrents = QueueEntry.select().reversed()
    return render_template('index.html', torrents=torrents)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = SubmitForm(request.form)
    if request.method == "POST" and form.validate():
        print form.link
        entry = QueueEntry(torrent=form.link.data)
        flash('Wurde ja Zeit')
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run()