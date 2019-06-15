import os
from . import db


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'test.sqlite3')


class Ranking(db.Model):
    __tablename__ = 'ranking'

    id = db.Column(db.Integer, primary_key=True)
    movieName = db.Column(db.String(56), nullable=False, index=True)
    movieImgPath = db.Column(db.String(), nullable=True)
    movieDescription = db.Column(db.String(256), nullable=False, index=True)

    def __repe__(self):
        return 'movie:{}, movieimg:{}, movieContent:{}'.format(self.__class__.movieName,
                        self.__class__.movieImgPath, self.movieDescription)


class MovieProfile(db.Model):
    __tablename__ = 'movieProfile'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    details = db.Column(db.String(256), nullable=False)
    stars = db.Column(db.String(8), nullable=False, index=True)
    director = db.Column(db.String(24), nullable=False)

    def __repe__(self):
        return 'Movie Profile, movieName: {}, movieDetails: {}, movieStars: {}, \
        movieDirector: {}'.format(self.__class__.name, self.__class__.details, self.__class__.stars, self.__class__.director)


class Comments(db.Model):
    __tablename__ = 'movieComments'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(24), nullable=False, index=True)
    date = db.Column(db.String(24), nullable=True)
    commentDetails = db.Column(db.String(512), nullable=False)

    def __repe__(self):
        return 'Comments, userName: {}, date: {}, commentDetails: {}'.format(self.__class__.userName,
                                                                             self.__class__.date, self.__class__.commentDetails)