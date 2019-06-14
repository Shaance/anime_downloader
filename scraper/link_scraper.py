import logging
import os
import platform
import time
from typing import List

from bs4 import BeautifulSoup, Tag
from selenium import webdriver

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


# TODO have to check if missing episodes

def get_links(mode: str, url: str, res: int) -> List[str]:
    links = []
    soup = BeautifulSoup(__get_page_source__(url), 'html.parser')

    link_containers = soup.find('div', attrs={'class': 'episode-container'}) \
        .find_all('div', attrs={'class': 'rls-link link-{}p'.format(res)})

    for link_container in link_containers:
        for elem in link_container.children:
            if isinstance(elem, Tag) and elem['class'] == ['dl-type', 'hs-{}-link'.format(mode)]:
                links.append(elem.contents[0]['href'])

    # we want to download the first episodes in priority
    links.reverse()

    return links


def __expand_episode_list__(browser) -> None:
    # pagination by default, have to expand all the episode list
    show_more_btn = browser.find_element_by_class_name("show-more")

    while show_more_btn.text != "No more results":
        browser.find_element_by_class_name("more-button").click()
        time.sleep(1)


def __get_page_source__(url: str):
    logging.info("Opening Chrome with the following URL %s.", url)
    # need to fire up a browser otherwise the links will not load with a simple urllib.open_url command

    browser = webdriver.Chrome(__get_chrome_driver__())
    browser.get(url)
    __expand_episode_list__(browser)

    page_source = browser.page_source
    browser.quit()
    return page_source


def __get_chrome_driver__():
    curr_platform = platform.system()
    drivers_directory = 'resources'
    if curr_platform == 'Darwin':
        return os.path.join(os.getcwd(), drivers_directory, 'chromedriver_osx')
    elif curr_platform == 'Linux':
        return os.path.join(os.getcwd(), drivers_directory, 'chromedriver_linux')
    else:
        os.path.join(os.getcwd(), drivers_directory, 'chromedriver.exe')
