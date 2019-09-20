from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
from urllib import robotparser
import os


class WorkWithURL(str):
    def get_name(self):
        """Извлекает имя для файла из url"""
        string_list = self.split('/')
        return string_list[2]

    def save_page(self):
        """Извлекает html и записывает в файл,сохраняемый в папке"""
        try:
            page = requests.get(self)
        except URLError:
            print("error")
            return
        data = page.text
        soup = BeautifulSoup(data).encode('utf-8')
        name_page = "{0}.html".format(WorkWithURL.get_name(self))
        directory = os.getcwd() + r"\pages"
        with open(os.path.join(directory, name_page), "wb") as page:
            page.write(soup)

    def get_soup(self):
        """Получаем soup через url"""
        page = requests.get(self)
        data = page.text
        soup = BeautifulSoup(data)
        return soup

    def process_robot_txt(self):
        """Обрабатываем файл robots.txt и возвращаем true или false в зависимости от того,можно ли нам краулить сайт"""
        rp = robotparser.RobotFileParser()
        try:
            rp.set_url(self + '/robots.txt')
            rp.read()
        except (URLError, UnicodeDecodeError):
            return True
        return rp.can_fetch('*', self)
