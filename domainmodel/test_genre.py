import pytest

from domainmodel.genre import Genre


class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_name is None

    def test___eq__(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        genre3 = Genre("Horror")
        assert genre1.__eq__(genre2) == False
        assert genre1.__eq__(genre3) == True

    def test___lt__(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        assert genre1.__lt__(genre2) == False

    def test_hash(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Horror")
        assert genre1.__hash__() == genre2.__hash__()
