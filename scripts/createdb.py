from model import QueueEntry

db_filename = os.path.abspath(app.config['DATABASE'])
if os.path.exists(db_filename):
    os.unlink(db_filename)
connection_string = 'sqlite:' + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

QueueEntry.createTable()