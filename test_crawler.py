from work_with_url import URLWorker
from work_with_links import LinksWorker
from threading import Thread
from queue import Queue
import requests
import bs4
import os.path
import unittest


class TestWorkWithURL(unittest.TestCase):

    def test_get_name(self):
        url = "https://www.google.ru"
        expected_name = "wwwgoogleru"
        actual_name = URLWorker.get_name(URLWorker(url))
        self.assertEqual(expected_name, actual_name)

    def test_get_soup(self):
        url = URLWorker("https://lenta.ru")
        actual = url.get_soup()
        page = requests.get("https://lenta.ru")
        data = page.text
        expected = bs4.BeautifulSoup(data)
        self.assertEqual(actual, expected)

    def test_save_page_error(self):
        url = URLWorker("https://lentabc.ru")
        actual = url.save_page("tests")
        self.assertEqual(actual, ConnectionError)

    def test_save_page(self):
        url = URLWorker("https://lenta.ru")
        url.save_page("tests")
        actual = os.path.isfile(r"tests\lentaru.html")
        self.assertEqual(actual, True)

    def test_robots_true(self):
        url = URLWorker("https://lenta.ru")
        actual = url.process_robot_txt()
        self.assertEqual(actual, True)

    def test_robot_false(self):
        url = URLWorker("https://github.com")
        actual = url.process_robot_txt()
        self.assertEqual(actual, False)

    def test_save_division_for_list(self):
        link = Queue()
        link.put("http://vilenin.narod.ru/Mm/Books/5/book.htm")
        thread = Thread()
        thread.start()
        URLWorker.save_division(thread, link, "tests")
        self.assertEqual(link.qsize(), 0)

    def test_save_division_download(self):
        link = Queue()
        link.put("http://vilenin.narod.ru/Mm/Books/5/book.htm")
        thread = Thread()
        thread.start()
        URLWorker.save_division(thread, link, "tests")
        actual = os.path.isfile(r"tests\httpvileninnarodruMmBooks5bookhtm.html")
        self.assertEqual(actual, True)


class TestWorkWithLinks(unittest.TestCase):

    def test_get_links_len(self):
        link = "http://vilenin.narod.ru/Mm/Books/5/book.htm"
        soup = URLWorker(link).get_soup()
        list_links = LinksWorker.get_links(soup)
        self.assertEqual(len(list_links), 2)

    def test_get_links_content(self):
        link = "http://vilenin.narod.ru/Mm/Books/5/book.htm"
        soup = URLWorker(link).get_soup()
        list_links = LinksWorker.get_links(soup)
        self.assertEqual(list_links[0], "http://top100.rambler.ru/top100/")
        self.assertEqual(list_links[1], "http://www.ucoz.ru/")
