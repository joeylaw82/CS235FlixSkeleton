import pytest

from domainmodel.actor import Actor


class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None

    def test___eq__(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Angelina Jolie")
        assert actor1.__eq__(actor2) == True
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Brad Pitt")
        assert actor1.__eq__(actor2) == False
    def test___lt__(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Brad Pitt")
        assert actor1.__lt__(actor2) == True
    def test_hash(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Angelina Jolie")
        assert actor1.__hash__() == actor2.__hash__()
    def test_add_actor_colleague(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Brad Pitt")
        actor1.add_actor_colleague(actor2)
        assert len(actor1.colleagueList) == 1
        assert actor1.colleagueList[0] == actor2
    def test_check_if_this_actor_worked_with(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Brad Pitt")
        actor3 = Actor("Jennifer Aniston")
        actor1.add_actor_colleague(actor2)
        assert actor1.check_if_this_actor_worked_with(actor2) == True
        assert actor1.check_if_this_actor_worked_with(actor3) == False


