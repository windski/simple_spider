import requests
from douban_parser import parse_context

urls = ["https://movie.douban.com/chart"]


def get_context(urls: list):
    result_html = []

    for i in urls:
        r = requests.get(i)
        result_html.append(r.text)

    return result_html


if __name__ == '__main__':
    c = get_context(urls)

    for i in c:
        parse_context(i)

