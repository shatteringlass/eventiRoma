#!/usr/bin/env python3


def scrape():
    import bs4
    import requests
    import datetime as dt

    url = 'http://www.romeguide.it/?pag=mostre'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    eventi = []

    for id in soup.find_all('div', id=lambda x: x and x.startswith('PGMOS')):
        for table in id.find_all('table'):
            for div in table.find_all('div', attrs={'align': 'left'}):
                item = div.get_text("|#|", strip=True).replace('\r\n', ' ')
                # parse item into "event_name", "location", "start_date", "end_date"
                list = item.split("|#|")
                date = list[2].split(" - ")
                parsed_item = {"event_name": list[0], "location": list[1],
                               "start_date": date[0], "end_date": date[1], "seen_time": dt.datetime.now()}
                # add parsed_item dict into database
                eventi.append(parsed_item)

    return eventi
