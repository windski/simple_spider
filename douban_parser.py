from bs4 import BeautifulSoup


def parse_context(context):
    soup = BeautifulSoup(context, 'lxml')
    rank_list_ = soup.find_all('table')[1:]

    nurls = []
    name_list = []
    img_list = []
    for i in rank_list_:
        nurls.append(i.a["href"])
        name_list.append(i.a["title"])
        img_list.append(i.img["src"])

    return nurls, name_list, img_list


def get_contextfrom_file():
    with open("./test.html", "r", encoding='UTF-8') as f:
        r = f.read()

    return r


if __name__ == '__main__':
    urls, name, img = parse_context(get_contextfrom_file())
    print(urls, name, img)
