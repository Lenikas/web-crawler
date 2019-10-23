from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
from urllib import robotparser
import os


class URLWorker(str):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_name(self):
        """Извлекает имя для файла из url"""
        string_for_name = self.replace("?", ".")
        string_list = string_for_name.split('/')
        if len(string_list) > 4:
            return string_list[2] + string_list[4]
        return string_list[2]

    def save_page(self):
        """Извлекает html и записывает в файл,сохраняемый в папке, если файл уже есть, то не скачивает повторно"""
        try:
            page = requests.get(self)
        except requests.exceptions.ConnectionError:
            print("Connection error")
            return ConnectionError
        data = page.text
        soup = BeautifulSoup(data).encode('utf-8')
        name_page = "{0}.html".format(URLWorker.get_name(self))
        directory = os.getcwd() + r"\pages"
        if os.path.isfile(os.path.join(directory, name_page)):
            print("This file is already exist")
            return
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
        except (URLError, UnicodeEncodeError):
            return True
        return rp.can_fetch('*', self)
