import os
from time import sleep
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
MSEDGEDRIVER_NAME = 'msedgedriver'
MSEDGEDRIVER_PATH = ROOT_PATH / 'bin' / MSEDGEDRIVER_NAME


def make_edge_browser(*options):
    edge_options = webdriver.EdgeOptions()

    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        edge_options.add_argument('--headless')

    edge_service = Service(executable_path=MSEDGEDRIVER_PATH)
    browser = webdriver.Edge(service=edge_service, options=edge_options)
    return browser


if __name__ == '__main__':
    browser = make_edge_browser('--headless')
    browser.get('http://www.google.com.br/')
    sleep(5)
