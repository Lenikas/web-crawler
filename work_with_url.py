import threading
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
from urllib import robotparser
import os
import re


class URLWorker(str):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_name(self):
        """Извлекает имя для файла из url"""
        string_for_name = self.replace("https://", "")
        return re.sub('[^a-zA-Z0-9]', '', string_for_name)

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
            return
        with open(os.path.join(directory, name_page), "wb") as page:
            page.write(soup)
        print("download" + " " + self)

    @staticmethod
    def save_division(thread, all_links_save):
        print(all_links_save)
        while thread.is_alive() or len(all_links_save) > 0:
            for link in all_links_save:
                all_links_save.remove(link)
                th = threading.Thread(target=URLWorker.save_page(link))
                th.start()
        while len(all_links_save) > 0:
            pass

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
        except (URLError, UnicodeEncodeError, UnicodeDecodeError):
            return True
        return rp.can_fetch('*', self)
