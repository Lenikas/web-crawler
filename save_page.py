import urllib.request
import sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def save_page(url):
    """
    Скачивает html страницы и записывает в файл с именем (после http://)
    """
    req = Request(
        url, headers={'User-Agent': 'Mozilla/5.0'})  # чтобы обойти блокировку
    html = urlopen(req).read()
    with open('{0}'.format(re.split(r'/', url)[2] + '.html'), "w") as file:
        file.write(str(html))
    return html


def get_links(html):
    soup = BeautifulSoup(html)
    links = soup.findAll('a', attrs={'href': re.compile("^http://")})
    #   links.append(soup.findAll('a'))
    only_http = re.findall(r'https?://\S+', str(links))
    print(only_http)
    return only_http


def recursive_url(url):
    del url[0]
    print(url[0])
    a = save_page(url[0])
    get_links(a)


if __name__ == "__main__":
    page = save_page(sys.argv[1])
    a = get_links(page)
    recursive_url(a)
