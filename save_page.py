from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html
import sys


def find_links(url):
    """
    Находит все ссылки на указанной странице и возвращает список из этих ссылок
    """
    #   main_url = "https://lecturesnet.readthedocs.io/net/web.scraping/lxml.html"
    re = requests.get(url)
    root = lxml.html.fromstring(re.content)
    page_links = [url + link for link in root.xpath('//a/@href')]
    print(page_links)
    return page_links


def recursive_find_url(list_links):
    for link in list_links:
        find_links(link)


def main():
    url = sys.argv[1]
    list_links = find_links(url)
    recursive_find_url(list_links)


if __name__ == '__main__':
    main()

