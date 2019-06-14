import re
from urllib.request import urlopen, Request
from typing import List

from bs4 import BeautifulSoup

from show import Show


def scrap_shows_url(domain: str) -> List[Show]:
    result = []
    soup = __get_soup__(domain + "/shows")
    for show in soup.find_all(href=__is_show__):
        result.append(Show(show['title'], "", domain + show['href'], ""))

    return result


def scrap_show_img_desc(show: Show, domain: str, show_url: str) -> Show:
    soup = __get_soup__(show_url)
    show.img = __scrap_show_image__(soup, domain)
    show.desc = __scrap_show_desc__(soup)

    return show


def __scrap_show_image__(soup: BeautifulSoup, domain: str) -> str:
    div = soup.find('div', attrs={'class': 'series-image'})
    img_src = div.contents[1]['src']
    if domain in img_src:
        return img_src
    else:
        return domain + img_src


def __scrap_show_desc__(soup: BeautifulSoup) -> str:
    div = soup.find('div', attrs={'class': 'series-desc'})
    return "".join(child.string for child in div.children if child and child.string
                   and child.string.lower() != 'description')


def __get_soup__(url: str) -> BeautifulSoup:
    source = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    return BeautifulSoup(source, "html.parser")


def __is_show__(href: str):
    return href and re.compile("^/shows/").search(href)
