from ost import ost
from ost.utilities import *
import pytest
import os


token = session.login("rlirey@gmail.com", "443182lotr")
tv_path = "./Game of Thrones - S01E01.m4v"
movie_path = "./Avengers - Age of Ultron.mp4"


tv = ost.TV()
movie = ost.MOVIE()
path = os.getcwd() + "/"


def test_class():
    assert type(tv) == ost.TV
    assert type(movie) == ost.MOVIE


def test_tv_search():
    tv.tv_search('./Game of Thrones - S01E01.m4v')
    assert tv.file
    assert tv.url
    assert tv.srt


def test_tv_download():
    tv.download(path)
    assert os.path.isfile('./Game of Thrones - S01E01.srt')


def test_movie_search():
    movie.movie_search('./Avengers - Age of Ultron.mp4')
    assert movie.file
    assert movie.url
    assert movie.srt


def test_movie_download():
    movie.download(path)
    assert os.path.isfile('./Avengers - Age of Ultron.srt')
