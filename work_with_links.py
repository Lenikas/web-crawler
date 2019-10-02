from work_with_url import WorkWithURL
import re
from threading import Thread


class WorkWithLinks:
    @staticmethod
    def get_links(soup):
        """Находим все ссылки в soup-e и собираем в список """
        list_links = []
        links = soup.find_all(attrs={'href': re.compile(r'(https?://[^\s]+)')})
        for link in links:
            if WorkWithURL.process_robot_txt(link.get('href')):
                list_links.append(link.get('href'))
            else:
                print("not allow")
        return list_links

    @staticmethod
    def save_list_links(list_links):
        for link in list_links:
            link = WorkWithURL(link)
            link.save_page()

    @staticmethod
    def recursive_find_url(list_links, max_depth=0):
        """Рекурсивный поиск ссылок"""
        if max_depth > 0:
            for link in list_links:
                print(link)
                link = WorkWithURL(link)
                soup = link.get_soup()
                links = WorkWithLinks.get_links(soup)
                WorkWithLinks.new_thread_download(links)
                WorkWithLinks.recursive_find_url(links, max_depth=max_depth - 1)

    @staticmethod
    def new_thread_download(list_links):
        """Создаем новы поток для загрузки нового листа ссылок"""
        thread = Thread(WorkWithLinks.save_list_links(list_links))
        thread.start()