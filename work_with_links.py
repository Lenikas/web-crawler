import sys

import work_with_url
import re
from queue import Queue
#from multiprocessing import Queue


class LinksWorker:
    all_links = Queue()

    @staticmethod
    def get_links(soup):
        """Находим все ссылки в soup-e и собираем в список """
        list_links = []
        links = soup.find_all(attrs={'href': re.compile(r'(https?://[^\s]+)')})
        for link in links:
            url = link.get('href')
            if work_with_url.URLWorker.process_robot_txt(url):
                list_links.append(url)
                LinksWorker.all_links.put(url)
                print(LinksWorker.all_links.qsize())
            else:
                print("not allow")
        return list_links

    @staticmethod
    def recursive_find_url(list_links, max_depth=0):
        """Рекурсивный поиск ссылок"""
        if max_depth > 0:
            for link in list_links:
                print(link)
                link = work_with_url.URLWorker(link)
                soup = link.get_soup()
                new_links = LinksWorker.get_links(soup)
                LinksWorker.recursive_find_url(new_links, max_depth=-1)




