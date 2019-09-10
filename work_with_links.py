from work_with_url import WorkWithURL
import re


class WorkWithLinks:
    @staticmethod
    def get_links(soup):
        """Находим все ссылки в soup-e и собираем в список """
        list_links = []
        for link in soup.find_all(attrs={'href': re.compile("http")}):
            list_links.append(link.get('href'))
        return list_links

    @staticmethod
    def recursive_find_url(list_links, max_depth=0):
        """Рекурсивный поиск ссылок"""
        if max_depth > 0:
            for link in list_links:
                link = WorkWithURL(link)
                link.save_page()
                print(link)
                soup = link.get_soup()
                links = WorkWithLinks.get_links(soup)
                WorkWithLinks.recursive_find_url(links, max_depth=max_depth - 1)