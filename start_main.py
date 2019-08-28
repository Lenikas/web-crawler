from save_page import save_page, get_soup, get_links, recursive_find_url, sys


def main():
    url = sys.argv[1]
    if len(sys.argv) == 3:
        max_depth = int(sys.argv[2])
    save_page(url)
    #max_depth = sys.argv[2]
    soup = get_soup(url)
    list_links = get_links(soup)
    recursive_find_url(list_links, max_depth)


if __name__ == "__main__":
    main()
