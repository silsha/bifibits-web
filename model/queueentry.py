from sqlobject import *
from datetime import datetime

class QueueEntry(SQLObject):
	putid = IntCol(default=None)
	name = UnicodeCol(default=None)
	size = IntCol(default=None)
	torrent = UnicodeCol()
	status = EnumCol(enumValues=['NEW', 'SUBMITTED', 'DOWNLOADING', 'DONE', 'ERROR'], default='NEW')
	error_reason = UnicodeCol(default=None)
	added_time = DateTimeCol(default=datetime.now)
	last_update = DateTimeCol(default=None)