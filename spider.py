import requests
import time
from douban_parser import parse_250_ranking, parse_context
from storage_file import storage_file
from connectdb import Ranking, create_session

url = "https://movie.douban.com/top250?start={}&filter="


def get_img_data(urls: str):
    time.sleep(1)
    r = requests.get(urls)
    return r.content


def get_context(urls: str):
    r = requests.get(urls)
    return r.text


def commit_movie_profile(session, urls: list):
    for i in urls:
        content = get_context(i)


if __name__ == '__main__':
    # create a connection with database
    session = create_session()
    commit_movie_profile(session, ["https://movie.douban.com/subject/1292052/"])
    exit(0)
    pages_item = 25
    start_item = 0

    # get page content
    for _ in range(10):
        start_item += pages_item
        c = get_context(url.format(start_item))
        name, img, content, profile_url = parse_250_ranking(c)

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
        commit_movie_profile(session, profile_url)

    # urls, name, img = parse_context(i)
    #
    # for j in range(len(img)):
    #     content = get_img_data(img[j])
    #     storage_file(name[j] + '.jpg', content)
