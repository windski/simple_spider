from bs4 import BeautifulSoup


def parse_context(content):
    soup = BeautifulSoup(content, 'lxml')
    rank_list_ = soup.find_all('table')[1:]

    nurls = []
    name_list = []
    img_list = []
    for i in rank_list_:
        nurls.append(i.a["href"])
        name_list.append(i.a["title"])
        img_list.append(i.img["src"])

    return nurls, name_list, img_list


# just for test
def get_contextfrom_file():
    with open("./test.html", "r", encoding='UTF-8') as f:
        r = f.read()

    return r


def parse_250_ranking(content):
    soup = BeautifulSoup(content, 'lxml')
    list_ = soup.find_all('li')[19:]

    img_list = []
    name_list = []
    content_list = []
    next_url = []
    for i in list_:
        img_list.append(i.img['src'])
        name_list.append(i.img['alt'])
        next_url.append(i.a['href'])
        content_list.append(i.p.contents[0])

    return name_list, img_list, content_list, next_url


def parse_movie_profile(content) -> (str, list, list, list):
    soup = BeautifulSoup(content, 'lxml')
    name = soup.find('h1').span.contents
    director = soup.find('span', class_='attrs').a.contents
    stars = soup.find('strong', class_='ll rating_num').contents
    try:
        details = soup.find('span', class_='short').span.contents
    except AttributeError:
        details = soup.find_all('div', class_='indent')[-1].span.contents
    # details = soup.find('span', class_='all hidden').contents

    return name[0], stars, details, director


def parse_comments(content):
    soup = BeautifulSoup(content, 'lxml')

    com = soup.find_all('div', class_='comment-item')

    username = []
    for i in com:
        username.append(i.a['title'])

    t = soup.find_all('span', class_='comment-time')
    comment_time = []
    for i in t:
        comment_time.append(i.contents)

    print(comment_time)

    # print(username, com)


if __name__ == '__main__':
    # _, img, _, _ = parse_250_ranking(get_contextfrom_file())

    # print(img[0].split('.')[-1])

    parse_comments(get_contextfrom_file())

