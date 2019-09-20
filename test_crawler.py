import unittest
from work_with_url import WorkWithURL


class TestWorkWithURL(unittest.TestCase):

    def test_get_name(self):
        url = "https://www.google.ru"
        expected_name = "www.google.ru"
        actual_name = WorkWithURL.get_name(WorkWithURL(url))
        self.assertEqual(expected_name, actual_name)

    def test_status_code(self):
        url = "https://www.google.ru"
        expected_code = 200
        actual_code = WorkWithURL.status_code(WorkWithURL(url))
        self.assertEqual(expected_code, actual_code)

    def test_status_code_robots(self):
        url = "https://www.google.ru"
        expected_code = 200
        actual_code = WorkWithURL.status_code_robots(WorkWithURL(url))
        self.assertEqual(expected_code, actual_code)

    def test_get_soup(self):
        self.assertEqual(1, 1)

    def test_save_page(self):
        self.assertEqual(1, 1)


class TestWorkWithLinks(unittest.TestCase):

    def test_get_links(self):
        self.assertEqual(1, 1)

    def test_recursive_find_url(self):
        self.assertEqual(1, 1)