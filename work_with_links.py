import work_with_url
import re


class LinksWorker:
    all_links = []
    all_links_save = []

    @staticmethod
    def get_links(soup):
        """Находим все ссылки в soup-e и собираем в список """
        list_links = []
        links = soup.find_all(attrs={'href': re.compile(r'(https?://[^\s]+)')})
        for link in links:
            if work_with_url.URLWorker.process_robot_txt(link.get('href')):
                list_links.append(link.get('href'))
                LinksWorker.all_links.append(link.get('href'))
                LinksWorker.all_links_save.append(link.get('href'))
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



