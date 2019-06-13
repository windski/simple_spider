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
        return 'movie:{}, movieimg:{}, movieContent:{}'.format(self.__class__.movieName, \
                        self.__class__.movieImgPath, self.movieDescription)


def MovieProfile(dbBase):
    id = Column(Integer, primary_key=True)


if __name__ == '__main__':
    # For running it firstly
    db_engine = create_engine('sqlite://' + db_path)
    dbBase.metadata.create_all(db_engine)

    # Session = create_session()
    #
    # test = Ranking(movieName='test', movieDescription="test content")
    # Session.add(test)
    #
    # Session.commit()
