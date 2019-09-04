from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html
import sys
import re
from urllib.request import urlopen


class WorkWithURL(str):
    def get_name(self):
        """Извлекает имя для файла из url"""
        # page = requests.get(url)
        # tree = html.fromstring(page.content)
        # names = [name.text_content().strip() for name in tree.cssselect('title')]
        string_list = self.split('/')
        return string_list[2]
        # return names


    def save_page(self):
        """Извлекает html и записывает в файл,сохраняемый в папке"""
        #html = urlopen(url).read()
        page = requests.get(self)
        data = page.text
        soup = BeautifulSoup(data).encode('utf-8')
        name_page = "{0}.html".format(WorkWithURL.get_name(self))
        with open(name_page, "wb") as page:
            page.write(soup)


    def get_soup(self):
        """Получаем soup через url"""
        page = requests.get(self)    
        data = page.text
        soup = BeautifulSoup(data)
        return soup


def get_links(soup):
    """Находим все ссылки в soup-e и собираем в список """
    list_links = []
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        list_links.append(link.get('href'))
    return list_links


def recursive_find_url(list_links, max_depth=0):
    """Рекурсивный поиск ссылок"""
    if max_depth > 0:
        for link in list_links:
            link = WorkWithURL(link)
            link.save_page()
            print(link)
            soup = link.get_soup()
            links = get_links(soup)
            recursive_find_url(links, max_depth=max_depth-1)



   