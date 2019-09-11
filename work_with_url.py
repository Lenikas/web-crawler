from bs4 import BeautifulSoup
import requests
from urllib import robotparser, parse


class WorkWithURL(str):
    def get_name(self):
        """Извлекает имя для файла из url"""
        string_list = self.split('/')
        return string_list[2]

    def save_page(self):
        """Извлекает html и записывает в файл,сохраняемый в папке"""
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

    def process_robot_txt(self):
        """Обрабатываем файл robots.txt и возвращаем true или false в зависимости от того,можно ли нам краулить сайт"""
        rp = robotparser.RobotFileParser()
        rp.set_url(parse.urljoin(self, 'robots.txt'))
        rp.read()
        return rp.can_fetch('*', self)

    def status_code_robots(self):
        """Возвращает статус страницы robots.txt для данного урла"""
        r = requests.get(self + "/robots.txt")
        print(r.status_code)
        return r.status_code

    def status_code(self):
        """Возвращает статус страницы данного урла"""
        r = requests.get(self)
        print(r.status_code)
        return r.status_code

    def create_link(self):
        if self[0:4] != "http":
            return "https://" + self
        return self







   