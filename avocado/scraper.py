import abc
import logging

import requests
import unicodedata
from bs4 import BeautifulSoup

from avocado.menus import JedalenTomiMenu


class Scraper(metaclass=abc.ABCMeta):
    url = None

    def scrape(self):
        logging.info(f'Scraping {self.__class__.__name__}')
        try:
            menu = self._scrape()
        except CantScrapeError as e:
            logging.error(e.args[0])
            menu = None
        else:
            logging.info(f'Successfully scraped {self.__class__.__name__}')
            logging.info(menu)
        return menu

    def clean(self, t, split=True):
        """
        Remove tabs, remove all notprintable chars, remove multiple white-spaces.
        :param t: Tag/str
        :param split: if return as list or str
        """
        dirt = t.text if hasattr(t, 'text') else t
        nfkc = unicodedata.normalize('NFKC', dirt)

        # remove \t
        # split and for all rows remove multiple spaces
        # then join/or return based on `split` arg
        text = nfkc.replace('\t', '')
        text = text.strip().split('\n')
        text = [' '.join(a.split()) for a in text]
        text = [a for a in text if a]

        return text if split else ' '.join(text)

    def _scrape(self):
        response = requests.get(self.url) # todo - use session
        soup = BeautifulSoup(response.content, 'html.parser')
        menu = self.parse(soup)
        return menu

    @abc.abstractmethod
    def parse(self, soup):
        pass


class MenuckaScraper(Scraper):

    def parse(self, soup):
        pass


class BistroScraper(Scraper):
    def parse(self, soup):
        pass


# custom scrapers

class JedalenTomiScraper(Scraper):
    url = 'http://www.jedalentomi.sk/'

    def parse(self, soup):
        menu_div = soup.select('.about-features')
        if len(menu_div) != 1:
            raise CantScrapeError('Can\'t find div .about-features in jedalen tomi.')

        # parse menu for 3e
        ps = menu_div[0].find_all('p')
        menu_3e = self.clean(ps[1])[0]

        # parse 2 soups
        soups = self.clean(ps[2])

        # parse main courses
        mains = self.clean(ps[4])[:-1]

        return JedalenTomiMenu(soups, mains, menu_3e)


class CantScrapeError(Exception):
    pass
