drop table if exists queue_entry;
create table queue_entry (
	id integer primary key autoincrement,
	putid integer,
	name text,
	torrent text not null,
	status integer not null,
	added_time timestamp not null,
	last_update timestamp,
	error_reason text,
	size integer
);