#!/usr/bin/env python3

def gen_cal():

    import icalendar as ics
    import datetime as dt

    OUTPUT = 'eventi_roma.ics'
    WEBSITENAME = 'www.romeguide.it'
    db = 'eventi.db'

    cal = ics.Calendar()

    f = open('last_run', 'r+')
    lastruntime = f.read().strip()
    f.close()

    # calendar preparation...

    cal.add("prodid", "-//Mostre ed eventi a Roma //" + WEBSITENAME + "//")
    cal.add("version", "2.0")

    # query database

    sql = "SELECT * FROM eventi where strftime('%s',added_datetime) > {}".format(lastruntime)

    import query_db as qdb

    records = qdb.fetch(db, sql)
    for record in records:
        event = ics.Event()
        event.add("summary", record[1])
        event.add("dtstart", dt.date.fromtimestamp(dt.datetime.strptime(record[3], "%Y-%m-%d %H:%M:%S").timestamp()))
        event.add("dtend", dt.date.fromtimestamp(dt.datetime.strptime(record[4], "%Y-%m-%d %H:%M:%S").timestamp()))
        event.add("dtstamp", dt.date.fromtimestamp(dt.datetime.strptime(record[6], "%Y-%m-%d %H:%M:%S.%f").timestamp()))
        event.add("location", record[2])
        cal.add_component(event)

    f = open(OUTPUT, 'wb')
    f.write(cal.to_ical())
    f.close

    lastruntime = dt.date.strftime(dt.datetime.now(),'%s')

    f = open('last_run', 'r+')
    f.truncate(0)
    f.write(lastruntime)
    f.close()


if __name__ == "__main__":
    gen_cal()