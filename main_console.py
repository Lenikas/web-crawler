from work_with_url import WorkWithURL
from work_with_links import WorkWithLinks
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Crawler")
    parser.add_argument('--startcrawler', nargs=2)
    return parser.parse_args()


def process_arguments(args):
    start_link = args[0]
    depth_search = 0
    if len(args) == 2:
        depth_search = int(args[1])
    else:
        print("get depth for search")
        exit(0)
    return start_link, depth_search


def start_crawler(data_for_start):
    depth_search = data_for_start[1]
    start_link = data_for_start[0]
    WorkWithURL.save_page(start_link)
    soup = WorkWithURL.get_soup(start_link)
    list_links = WorkWithLinks.get_links(soup)
    WorkWithLinks.recursive_find_url(list_links, depth_search)


def main():
    args = parse_args()
    if args.startcrawler:
        data_for_start = process_arguments(args.startcrawler)
        start_crawler(data_for_start)
    else:
        print("error")


if __name__ == "__main__":
    main()
