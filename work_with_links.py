import work_with_url
import re
import queue
import logging


class LinksWorker:
    all_links = queue.Queue()
    dict_for_graph = {}
    logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO)
    log = logging.getLogger("info")

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
            else:
                LinksWorker.log.info("not allow {0}".format(url))
        return list_links

    @staticmethod
    def recursive_find_url(list_links, max_depth):
        """Рекурсивный поиск ссылок"""
        if max_depth > 0:
            for link in list_links:
                LinksWorker.log.info("process {0}".format(link))
                link = work_with_url.URLWorker(link)
                soup = link.get_soup()
                new_links = LinksWorker.get_links(soup)
                LinksWorker.dict_for_graph[link] = new_links
                LinksWorker.recursive_find_url(new_links, max_depth=max_depth - 1)




