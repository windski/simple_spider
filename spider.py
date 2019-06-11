import requests
from douban_parser import parse_context
from storage_file import storage_file

urls = ["https://movie.douban.com/chart"]


def get_img_data(urls):
    r = requests.get(urls)
    return r.content


def get_context(urls: list):
    result_html = []

    for i in urls:
        r = requests.get(i)
        result_html.append(r.text)

    return result_html


if __name__ == '__main__':
    c = get_context(urls)

    for i in c:
        urls, name, img = parse_context(i)

        for j in range(len(img)):
            content = get_img_data(img[j])
            storage_file(name[j] + '.jpg', content)
