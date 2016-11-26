import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import *


class TestDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.comic_db = ComicDB()
        self.comic_db.create()
        s = self.comic_db.get_session()
        series = Series(title="Sandman")

        s.add(series)
        s.commit()

        artist1 = Artist(name="Neil Gaiman")
        artist2 = Artist(name="Inker")
        comic = Comic(title="Sandman")
        comic.series = series.id

        s.add(artist1)
        s.add(artist2)
        s.add(comic)

        role = Role()
        role.artist = artist1
        role.comic = comic
        s.add(role)
        role = Role()
        role.artist = artist2
        role.comic = comic
        s.add(role)
        s.commit()

    def test_get_comic(self):
        s = self.comic_db.get_session()

        found = s.query(Comic).filter(Comic.title == "Sandman").one()
        assert found.title == "Sandman"
        assert found.artists != []

    @unittest.skip
    def test_get_artist(self):
        s = self.comic_db.get_session()

        found = s.query(Artist).filter(Artist.name == "Neil Gaiman").one()
        assert found.name == "Neil Gaiman"
        assert found.comics != []

    @unittest.skip
    def test_get_artist_by_comic(self):
        s = self.comic_db.get_session()
        result = s.query(Comic).filter(Comic.title == "Sandman").one()
        artists = set(x.artist.name for x in result.artists)
        assert artists == set(["Neil Gaiman", "Inker"])
