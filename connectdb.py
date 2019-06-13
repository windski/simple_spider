from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, String, Integer

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'test.sqlite3')


def create_session():
    db_engine = create_engine('sqlite:///' + db_path)
    session = sessionmaker(bind=db_engine)
    Session = session()

    return Session


dbBase = declarative_base()


class Ranking(dbBase):
    __tablename__ = 'ranking'

    id = Column(Integer, primary_key=True)
    movieName = Column(String(56), nullable=False, index=True)
    movieImgPath = Column(String(), nullable=True)
    movieDescription = Column(String(256), nullable=False, index=True)

    def __repe__(self):
        return 'movie:{}, movieimg:{}, movieContent:{}'.format(self.__class__.movieName,
                        self.__class__.movieImgPath, self.movieDescription)


class MovieProfile(dbBase):
    __tablename__ = 'movieProfile'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    details = Column(String(256), nullable=False)
    stars = Column(String(8), nullable=False, index=True)
    director = Column(String(24), nullable=False)

    def __repe__(self):
        return 'Movie Profile, movieName: {}, movieDetails: {}, movieStars: {}, \
        movieDirector: {}'.format(self.__class__.name, self.__class__.details, self.__class__.stars, self.__class__.director)


class Comments(dbBase):
    __tablename__ = 'movieComments'

    id = Column(Integer, primary_key=True)
    userName = Column(String(24), nullable=False, index=True)
    date = Column(String(24), nullable=True)
    commentDetails = Column(String(512), nullable=False)


if __name__ == '__main__':
    # For running it firstly
    db_engine = create_engine('sqlite:///' + db_path)
    dbBase.metadata.create_all(db_engine)

    # Session = create_session()
    #
    # test = Ranking(movieName='test', movieDescription="test content")
    # Session.add(test)
    #
    # Session.commit()
