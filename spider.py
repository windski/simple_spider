import requests
import time
from douban_parser import parse_250_ranking, parse_context
from storage_file import storage_file
from connectdb import Ranking, create_session

url = "https://movie.douban.com/top250?start=0&filter="


def get_img_data(urls):
    r = requests.get(urls)
    return r.content


def get_context(urls: list):
    r = requests.get(urls)
    return r.text


if __name__ == '__main__':
    # create a connection with database
    session = create_session()

    # get page content
    c = get_context(url)
    name, img, content, _ = parse_250_ranking(c)

    for i in range(len(name)):
        # storage the image data firstly.
        time.sleep(1)
        imgdata = get_img_data(img[i])
        posfix = img[i].split('.')[-1]
        imgpath = storage_file(name[i] + '.' + posfix, imgdata)

        rank = Ranking(movieName=name[i], movieImgPath=imgpath, movieDescription=content[i])
        session.add(rank)

    # So, U just storage all the data. it need commit to database
    session.commit()

    # urls, name, img = parse_context(i)
    #
    # for j in range(len(img)):
    #     content = get_img_data(img[j])
    #     storage_file(name[j] + '.jpg', content)
