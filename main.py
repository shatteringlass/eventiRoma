import scraper
import persist
import dl_ics


def main():
    persist.persist(scraper.scrape())
    dl_ics.gen_cal(cal_file='eventi_roma.ics', db='eventi.db')


if __name__ == '__main__':
    main()
