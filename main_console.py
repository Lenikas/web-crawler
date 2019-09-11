from work_with_url import WorkWithURL
from work_with_links import WorkWithLinks
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Crawler")
    parser.add_argument('--startcrawler',nargs=2)
    return parser.parse_args()


def process_arguments(args):
    start_link = args[0]
    if len(args) == 2:
        depth_search = int(args[1])
    else:
        print("get depth for search")
        exit(0)
    WorkWithURL.save_page(start_link)
    soup = WorkWithURL.get_soup(start_link)
    list_links = WorkWithLinks.get_links(soup)
    WorkWithLinks.recursive_find_url(list_links, depth_search)


def main():
    args = parse_args()
    if args.startcrawler:
        process_arguments(args.startcrawler)
    else:
        print("error")



if __name__ == "__main__":
    main()
