from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from declarations import Base


class ComicDB(object):
    def __init__(self):
        self.engine = create_engine("sqlite:///",echo=True)

        self.sessionmaker = sessionmaker(bind=self.engine)

    def create(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.sessionmaker()
