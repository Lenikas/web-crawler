from save_page import get_links, recursive_find_url, sys
from save_page import WorkWithURL


def main():
    url = sys.argv[1]
    url = WorkWithURL(url)
    if len(sys.argv) == 3:
        max_depth = int(sys.argv[2])
    url.save_page()
    #max_depth = sys.argv[2]
    soup = url.get_soup()
    list_links = get_links(soup)
    recursive_find_url(list_links, max_depth)


if __name__ == "__main__":
    main()
