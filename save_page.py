import urllib.request
import sys
from bs4 import BeautifulSoup
import urllib


def save_page(url):
    html = urllib.request.urlopen(url).read()
    f = open('index.html', 'w')
    f.write(str(html))
    f.close()


def recursive_url(url, depth):
    if depth == 5:
        return url
    else:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read())
        newlink = soup.find('a') #  шаблон для ссылок сделать
        if len(newlink) == 0:
            return url
        else:
            return url, recursive_url(newlink, depth+1)


def get_links(url):
    page = urllib.request.urlopen(url)
    soup = (page.read())
    links = soup.find_all('a', {'class': 'institution'})
    for link in links:
        links.append(recursive_url(link, 0))
    return links


if __name__ == "__main__":
    save_page(sys.argv[1])
