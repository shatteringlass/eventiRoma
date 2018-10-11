#!/usr/bin/env python3

def persist(eventi, dbfile='eventi.db'):
    import sqlite3 as sl3
    import datetime as dt

    conn = sl3.connect(dbfile)
    c = conn.cursor()
    crt_statement = '''create table if not exists eventi
    (id integer not null primary key autoincrement, event_name text not null, location text, start_date text,
     end_date text, url text, scrape_datetime text, added_datetime text)'''

    c.execute(crt_statement)
    conn.commit()


    for e in eventi:
        row = [
            e.get('event_name'),
            e.get('location'),
            dt.datetime.strptime(e.get('start_date'), "%d/%m/%Y"),
            dt.datetime.strptime(e.get('end_date'), "%d/%m/%Y"),
            e.get('seen_time'),
            dt.datetime.now()
        ]
        c.execute(
            '''insert into eventi values (NULL, ?, ?, ?, ?, NULL, ?, ?)''', row
        )

    conn.commit()
    conn.close()
