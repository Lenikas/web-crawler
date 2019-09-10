from bs4 import BeautifulSoup
import requests


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






   