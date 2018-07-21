import logging
from datetime import datetime

import requests
from slacky import SlackMessage

import avocado.scraper
import avocado.settings
from avocado.slack import MenuSlackAttachment


def start():
    today = datetime.today().strftime('%d.%m.%Y')
    scrapers = [scraper.JedalenTomiScraper(), ]
    menus = []

    # scrape menus
    for sc in scrapers:
        menu = sc.scrape()
        menus.append(menu)

    # send menus to slack
    attachments = [MenuSlackAttachment(menu) for menu in menus]
    message = SlackMessage(f'Here\'s daily menu for *{today}*', attachments)
    requests.post(settings.SLACK_API_WEBHOOK, json=message.as_dict())


def main():
    logging.info('Avocado started scraping daily-menus.')
    start()
    logging.info('Avocado ended scraping daily-menus.')
