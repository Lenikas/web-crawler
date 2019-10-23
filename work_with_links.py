from work_with_url import URLWorker
import re
from threading import Thread


class LinksWorker:
    global_list = []
    @staticmethod
    def get_links(soup):
        """Находим все ссылки в soup-e и собираем в список """
        list_links = []
        links = soup.find_all(attrs={'href': re.compile(r'(https?://[^\s]+)')})
        for link in links:
            if URLWorker.process_robot_txt(link.get('href')):
                list_links.append(link.get('href'))
            else:
                print("not allow")
        return list_links

    @staticmethod
    def save_list_links(link_for_download):
        link = URLWorker(link_for_download)
        link.save_page()
        global global_list
        global_list.remove(0)

    @staticmethod
    def recursive_find_url(list_links, max_depth=0):
        """Рекурсивный поиск ссылок"""
        if max_depth > 0:
            for link in list_links:
                print(link)
                link = URLWorker(link)
                soup = link.get_soup()
                links = LinksWorker.get_links(soup)
                for new_link in links:
                    global global_list
                    global_list.append(new_link)
                LinksWorker.recursive_find_url(links, max_depth=max_depth - 1)


    @staticmethod
    def new_thread_download(link):
        """Создаем новы поток для загрузки нового листа ссылок"""
        thread = Thread(LinksWorker.save_list_links(link))
        thread.start()