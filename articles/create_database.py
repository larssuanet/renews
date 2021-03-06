from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, DateTime
from dotenv import load_dotenv
import os
from sqlalchemy import Column, Integer, String, Boolean
import datetime

load_dotenv()

PG_DATABASE = os.getenv("PG_DATABASE")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")

connection_string = "postgresql://" + PG_USER + ":" + PG_PASSWORD + "@" + PG_HOST + ":" + PG_PORT + "/" + PG_DATABASE
engine = create_engine(connection_string, echo=True)

Base = declarative_base()


class NewsSource(Base):
	__tablename__ = 'news_source'

	id = Column(Integer, primary_key=True)
	name = Column(String(128))
	country_code = Column(String(2))
	base_url = Column(String(256))
	created = Column(DateTime, default=datetime.datetime.now)
	last_updated = Column(DateTime, onupdate=datetime.datetime.now)


class Article(Base):
	__tablename__ = 'article'

	id = Column(Integer, primary_key=True)
	news_source_id = Column(Integer, ForeignKey('news_source.id'))
	article_id = Column(Integer)
	is_article = Column(Boolean)
	last_updated = Column(DateTime, onupdate=datetime.datetime.now)
	title = Column(String(256))
	body_file_path = Column(String(256))
	url = Column(String(256))
	category = Column(String(64))
	article_published = Column(DateTime)
	created = Column(DateTime, default=datetime.datetime.now)
	article_last_updated = Column(DateTime)


class Scrape(Base):
	__tablename__ = 'scrape'

	id = Column(Integer, primary_key=True)
	news_source_id = Column(Integer, ForeignKey('news_source.id'))
	success = Column(Boolean)
	article_id = Column(Integer, ForeignKey('article.id'), nullable=True)
	message = Column(String(256))
	url = Column(String(256))
	created = Column(DateTime, default=datetime.datetime.now)


Base.metadata.create_all(engine)
