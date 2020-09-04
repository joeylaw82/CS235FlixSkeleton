import pytest

from activitysimulations.watchingsimulation import MovieWatchingSimulation
from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review


class Testwatchingsimulator:

    def test_init(self):
        movie = Movie("Moana", 2016)
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        user4 = User('Martin', 'pw12345')
        user_list = [user2, user3, user4]
        watch = MovieWatchingSimulation(user_list, movie)
        assert repr(
            watch) == "Movie watching : <Movie Moana, 2016>\nUser(s) watching : [<User ian>, <User daniel>, <User martin>]\nReview : None"

    def test_add_review(self):
        movie = Movie('Moana', 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        user4 = User('Martin', 'pw12345')
        user_list = [user2, user3, user4]
        watch = MovieWatchingSimulation(user_list, movie)
        watch.add_review(review_text, rating)
        assert (watch.review != None) == True

