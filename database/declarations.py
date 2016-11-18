from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = "role"
    # id = Column(Integer, primary_key=True)
    comic_id = Column(Integer, ForeignKey("comic.id"), primary_key=True)
    artist_id = Column(Integer, ForeignKey("artist.id"), primary_key=True)

    comic = relationship("Comic", back_populates="artists")
    artist = relationship("Artist", back_populates="comics")


class Comic(Base):
    __tablename__ = "comic"
    id = Column(Integer, primary_key=True)
    artists = relationship("Role", back_populates="comic")

    date = Column(Date)
    title = Column(String)


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True)
    comics = relationship("Role", back_populates="artist")

    name = Column(String)
