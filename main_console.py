from threading import Thread
from work_with_url import URLWorker
from work_with_graph import GraphWorker
from work_with_threads import ThreadWorker
from work_with_links import LinksWorker
from bokeh.io import output_file, save
import argparse
import sys
import re


def create_filters():
    list_regex = []
    dict_filters = dict.fromkeys(["only_https", "only_http", "http_and_https", "social_links"])
    with open("filters.txt", "r") as file:
        for line in file:
            list_regex.append(line.replace("\n", ""))
    index = 0
    for key in dict_filters:
        dict_filters[key] = list_regex[index]
        index += 1
        if index == len(list_regex):
            return dict_filters


def parse_args():
    """Парсим аргументы для аргпарса"""
    parser = argparse.ArgumentParser(description="Crawler")
    parser.add_argument('--startcrawler', nargs="*",
                        help=r"python main_console --startcrawler {link for start} {depth for search} {count threads} {filter},"
                             r"you have two variants of starting :"
                             r"1)without depth, count and filter, this parameters have default values(0 for depth, 1 for threads and filter for https links)"
                             r"2)you can write these free parameters, any for depth and count, for filters now is 4 variants:"
                             r"only_https, only_http, http_and_https, social_links")
    return parser.parse_args()


def start_crawler(start_link, depth, count_threads, selection):
    """Запуск краулера"""
    graph = GraphWorker()
    graph.add_node(start_link)

    URLWorker.save_page(start_link, "pages")
    soup = URLWorker.get_soup(start_link)
    links = LinksWorker.get_links(soup, selection)
    graph.create_base_graph(links, start_link)

    main_thread = Thread(target=LinksWorker.recursive_find_url, args=(links, selection, depth))
    list_thread = []
    for i in range(count_threads):
        thread_download = Thread(name=str(i), target=URLWorker.save_division,
                                 args=(main_thread, LinksWorker.all_links, "pages"))
        list_thread.append(thread_download)
    all_threads = ThreadWorker(main_thread, list_thread)
    all_threads.main_thread.start()
    all_threads.start_threads()
    all_threads.main_thread.join()
    all_threads.joined_threads()

    graph.create_graph(LinksWorker.dict_for_graph)
    plot = GraphWorker.rendering_graph(graph)
    output_file("graph.html")
    save(plot)


def main():
    sys.setrecursionlimit(10000)
    args = parse_args()
    dict_filters = create_filters()
    if args.startcrawler:
        if len(args.startcrawler) == 1:
            start_link = args.startcrawler[0]
            depth = 0
            count_threads = 1
            selection = r"https?://[^\s]+"
        elif len(args.startcrawler) == 4:
            start_link = args.startcrawler[0]
            depth = int(args.startcrawler[1])
            count_threads = int(args.startcrawler[2])
            selection = dict_filters[str(args.startcrawler[3])]
        else:
            raise SyntaxError("usage: main_console.py [-h] [--startcrawler STARTCRAWLER STARTCRAWLER]")
        start_crawler(start_link, depth, count_threads, selection)
    else:
        raise SyntaxError("usage: main_console.py [-h] [--startcrawler STARTCRAWLER STARTCRAWLER]")


if __name__ == "__main__":
    main()
