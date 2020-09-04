import pytest

from domainmodel.director import Director


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test___eq__(self):
        director1 = Director("Taika Waititi")
        director2 = Director("Taika Waititi")
        assert director1.__eq__(director2) == True
        director1 = Director("Taika Waititi")
        director2 = Director("Taika Waitit")
        assert director1.__eq__(director2) == False
        director1 = Director("Taika Waititi")
        director2 = Director("abcde ghjtiti")
        assert director1.__eq__(director2) == False
    def test___lt__(self):
        director1 = Director("Taika Waititi")
        director2 = Director("Taika Waititi")
        assert director1.__lt__(director2) == False
        director1 = Director("Taika Waititi")
        director2 = Director("Z")
        assert director1.__lt__(director2) == True
        director2 = Director("Taika Waititi")
        director1 = Director("aaa")
        assert director1.__lt__(director2) == False
    def test_hash(self):
        director1 = Director("Taika Waititi")
        director2 = Director("Taika Waititi")
        assert director1.__hash__() == director2.__hash__()

