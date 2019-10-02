import unittest
from work_with_url import WorkWithURL
import requests
import bs4
import os.path


class TestWorkWithURL(unittest.TestCase):

    def test_get_name(self):
        url = "https://www.google.ru"
        expected_name = "www.google.ru"
        actual_name = WorkWithURL.get_name(WorkWithURL(url))
        self.assertEqual(expected_name, actual_name)

    def test_get_soup(self):
        url = WorkWithURL("https://lenta.ru")
        actual = url.get_soup()
        page = requests.get("https://lenta.ru")
        data = page.text
        expected = bs4.BeautifulSoup(data)
        self.assertEqual(actual, expected)

    def test_save_page_error(self):
        url = WorkWithURL("https://lentabc.ru")
        actual = url.save_page()
        self.assertEqual(actual, ConnectionError)

    def test_save_page(self):
        url = WorkWithURL("https://lenta.ru")
        url.save_page()
        actual = os.path.isfile(r"pages\lenta.ru.html")
        self.assertEqual(actual, True)

    def test_robots_true(self):
        url = WorkWithURL("https://lenta.ru")
        actual = url.process_robot_txt()
        self.assertEqual(actual, True)

    def test_robot_false(self):
        url = WorkWithURL("https://github.com")
        actual = url.process_robot_txt()
        self.assertEqual(actual, False)


class TestWorkWithLinks(unittest.TestCase):

    def test_get_links(self):
        self.assertEqual(1, 1)

    def test_recursive_find_url(self):
        self.assertEqual(1, 1)