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
    # links = soup.findAll('a') находит еще и href
    only_http = re.findall(r'https?://\S+', str(links[0]))
    print(only_http)
    return only_http

def recursive_url(url, depth):
    if depth == 5:
        return url
    else:
        page=urllib.request.urlopen(url)
        soup=BeautifulSoup(page.read())
        newlink=soup.find('a')
        if len(newlink) == 0:
            return url
        else:
            return url, recursive_url(newlink, depth+1)


if __name__ == "__main__":
    page=save_page(sys.argv[1])
    get_links(page)
