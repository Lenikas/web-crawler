from threading import Thread
from work_with_url import URLWorker
from work_with_links import LinksWorker
import argparse


def parse_args():
    """Парсим аргументы для аргпарса"""
    parser = argparse.ArgumentParser(description="Crawler")
    parser.add_argument('--startcrawler', nargs=2,
                        help=r"python main_console --startcrawler {link for start} {depth for search}")
    return parser.parse_args()


def start_crawler(start_link, depth):
    """Запуск краулера"""
    URLWorker.save_page(start_link)
    soup = URLWorker.get_soup(start_link)
    links = LinksWorker.get_links(soup)
    thread1 = Thread(target=LinksWorker.recursive_find_url(links, depth))
    thread2 = Thread(target=URLWorker.save_division(thread1, LinksWorker.all_links_save))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


def main():
    args = parse_args()
    if args.startcrawler:
        start_link = args.startcrawler[0]
        depth = int(args.startcrawler[1])
        start_crawler(start_link, depth)
    else:
        raise SyntaxError("usage: main_console.py [-h] [--startcrawler STARTCRAWLER STARTCRAWLER]")


if __name__ == "__main__":
    main()
