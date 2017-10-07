#!/usr/bin/env python3

def gen_cal():

    import iCalendar as ics

    OUTPUT = 'eventi_roma.ics'
    WEBSITENAME = 'www.romeguide.it'

    cal = ics.Calendar()

    # calendar preparation...

    cal.add("prodid", "-//Mostre ed eventi a Roma //" + WEBSITENAME + "//")
    cal.add("version", "2.0")

    # query database

    sql = "()"

    import query_db as dqb

    records = qdb.fetch(sql)
    for record in records:
        event = ics.event()
        event.add("summary": )
        event.add("dtstart": )
        event.add("dtend": )
        event.add("dtstamp": )
        event.add("location": )
        cal.add_component(event)

    f = open (OUTPUT, 'wb')
    f.write(cal.to_ical())
    f.close


if __name__ == "__main__":
    gen_cal()