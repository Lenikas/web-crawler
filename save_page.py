from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html
import sys
import re
from urllib.request import urlopen


def get_name(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    names = [name.text_content().strip() for name in tree.cssselect('title')]
    return names


def save_page(url):
    #html = urlopen(url).read()
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data).encode('utf-8')
    name_page = "{0}.html".format(get_name(url))
    with open(name_page, "wb") as page:
        page.write(soup)


def get_soup(url):
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data)
    return soup


def get_links(soup):
    list_links = []
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        list_links.append(link.get('href'))
    return list_links


def recursive_find_url(list_links, max_depth=2):
    if max_depth > 0:
        for link in list_links:
            save_page(link)
            print(link)
            soup = get_soup(link)
            links = get_links(soup)
            recursive_find_url(links, max_depth=max_depth-1)


def main():
    url = sys.argv[1]
    save_page(url)
    #max_depth = sys.argv[2]
    soup = get_soup(url)
    list_links = get_links(soup)
    recursive_find_url(list_links)
    
   
if __name__ == '__main__':
    main()
