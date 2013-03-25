drop table if exists torrents;
create table torrents (
	id integer primary key autoincrement,
	putid integer,
	name text,
	torrent text not null,
	status integer not null,
	added_time timestamp not null,
	lastupdate timestamp,
	size integer
);