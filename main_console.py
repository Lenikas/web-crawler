import sys
from threading import Thread
from work_with_url import URLWorker
from work_with_links import LinksWorker
import argparse


def parse_args():
    """Парсим аргументы для аргпарса"""
    parser = argparse.ArgumentParser(description="Crawler")
    parser.add_argument('--startcrawler', nargs="*",
                        help=r"python main_console --startcrawler {link for start} {depth for search},"
                             r"default value for depth is 1")
    return parser.parse_args()


def start_crawler(start_link, depth):
    """Запуск краулера"""
    URLWorker.save_page(start_link, "pages")
    soup = URLWorker.get_soup(start_link)
    links = LinksWorker.get_links(soup)
    thread1 = Thread(target=LinksWorker.recursive_find_url, args=(links, depth))
    thread1.start()
    list_thread = []
    for i in range(4):
        thread_download = Thread(name=str(i), target=URLWorker.save_division,
                                 args=(thread1, LinksWorker.all_links, "pages", i))
        list_thread.append(thread_download)
        print(list_thread)
        thread_download.start()
    thread1.join()
    for thread in list_thread:
        print(list_thread)
        print(LinksWorker.all_links.qsize())
        print("aaaaaaaaaa")

        thread.join()


def main():
    args = parse_args()
    if args.startcrawler:
        if len(args.startcrawler) < 2:
            start_link = args.startcrawler[0]
            depth = 1
        else:
            start_link = args.startcrawler[0]
            depth = int(args.startcrawler[1])
        start_crawler(start_link, depth)
    else:
        raise SyntaxError("usage: main_console.py [-h] [--startcrawler STARTCRAWLER STARTCRAWLER]")


if __name__ == "__main__":
    main()
