from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
from urllib import robotparser
import os
import re
import logging


class URLWorker(str):

    logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO)
    log = logging.getLogger("info")

    def get_name(self):
        """Извлекает имя для файла из url"""
        string_for_name = self.replace("https://", "")
        return re.sub('[^a-zA-Z0-9]', '', string_for_name)

    def save_page(self, folder):
        """Извлекает html и записывает в файл,сохраняемый в папке, если файл уже есть, то не скачивает повторно"""
        try:
            page = requests.get(self)
        except requests.exceptions.ConnectionError:
            URLWorker.log.info("Connection error {0}".format(self))
            return ConnectionError
        data = page.text
        soup = BeautifulSoup(data).encode('utf-8')
        name_page = "{0}.html".format(URLWorker.get_name(self))[:255]
        directory = os.path.join(os.getcwd(), folder)
        if os.path.isfile(os.path.join(directory, name_page)):
            return
        try:
            with open(os.path.join(directory, name_page), "wb") as page:
                page.write(soup)
        except FileNotFoundError:
            return
        URLWorker.log.info("download {0}".format(self))

    @staticmethod
    def save_division(thread, all_links, directory):
        """Пока работает главный тред по поиску ссылок или очередь еще не пуста, продолжаем загрузку"""
        while thread.isAlive() or all_links.qsize() > 0:
            link = all_links.get()
            if link is None:
                break
            URLWorker.save_page(link, directory)
            all_links.task_done()

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
