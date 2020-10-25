from datetime import date, datetime
from typing import List
import os

import pytest

import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from adapters import memory_repository
from adapters.memory_repository import MemoryRepository
from adapters.repository import AbstractRepository, RepositoryException
from domainmodel.user import User
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre

TEST_DATA_PATH = os.path.join('Macintosh HD', os.sep, 'Users', 'joeylaw', 'CS235FlixSkeleton',
                              'datafiles')


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(TEST_DATA_PATH, repo)
    return repo


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    assert number_of_movies == 1000


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie("testing", 2020)
    movie.rank = 1001
    in_memory_repo.add_movie(movie)

    assert in_memory_repo.get_movie(1001) is movie


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1)

    # Check that the movie has the expected title.
    assert movie.title == 'Guardians of the Galaxy'

    # Check that the movie is commented as expected.
    review_1 = movie.reviews[0]
    assert review_1.user.user_name == 'thorke'
    # Check that the movie is tagged as expected.
    assert (movie in in_memory_repo.get_movie_by_actor('Chris Pratt')) == True
    assert (movie in in_memory_repo.get_movie_by_genre('Sci-Fi')) == True
    assert (movie in in_memory_repo.get_movie_by_director('James Gunn')) == True


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1001)
    assert movie is None


def test_repository_can_get_first_movie_by_rank(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == 'Guardians of the Galaxy'


def test_repository_can_get_last_movie_by_rank(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == 'Nine Lives'


def test_repository_can_get_movie_by_actor(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_actor('Paul Walker')
    movie_in_list = in_memory_repo.get_movie(320)
    assert (movie_in_list in matched_movie) == True


def test_repository_can_get_movie_by_actor_list(in_memory_repo):
    actor_name_list = ['paul walker', 'vin diesel']
    matched_movie = in_memory_repo.get_movie_by_actor_list(actor_name_list)
    assert len(matched_movie) == 4


def test_repository_does_not_get_movie_by_actor_if_actor_not_exist(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_actor('Joey')
    assert (matched_movie == []) == True


def test_repository_can_get_movie_by_director(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_director('Justin Lin')
    movie_in_list = in_memory_repo.get_movie(320)
    assert (movie_in_list in matched_movie) == True


def test_repository_does_not__get_movie_by_director_if_director_not_exist(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_director('Joey')
    assert (matched_movie == []) == True


def test_repository_can_get_movie_by_genre(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_genre('Action')
    movie_in_list = in_memory_repo.get_movie(320)
    assert (movie_in_list in matched_movie) == True


def test_repository_can_get_movie_by_genre_list(in_memory_repo):
    genre_name_list = ['action', 'romance']
    matched_movie = in_memory_repo.get_movie_by_genre_list(genre_name_list)
    assert len(matched_movie) == 7


def test_repository_does_not_get_movie_by_genre_if_genre_not_exist(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_genre('Crazy')
    assert (matched_movie == []) == True


def test_repository_can_get_movie_by_title(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_title('Fast')
    movie_in_list = in_memory_repo.get_movie(320)
    assert (movie_in_list in matched_movie) == True


def test_repository_does_not_get_movie_by_title_if_title_not_exist(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_title('***********')
    assert (matched_movie == []) == True


def test_repository_can_get_movie_by_release_year(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_release_year(2011)
    movie_in_list = in_memory_repo.get_movie(320)
    assert (movie_in_list in matched_movie) == True


def test_repository_does_not_get_movie_by_release_year_not_exist(in_memory_repo):
    matched_movie = in_memory_repo.get_movie_by_release_year(2222)
    assert (matched_movie == []) == True


def test_repository_can_add_actor_and_get_users_stored_in_repository(in_memory_repo):
    actor = Actor('Joey Law')
    in_memory_repo.add_actor(actor)
    actors = in_memory_repo.get_actors()
    assert (actor in actors) == True


def test_repository_does_not_add_actor_if_parameter_is_not_actor_type(in_memory_repo):
    actor = 'Joey Law'
    in_memory_repo.add_actor(actor)
    actors = in_memory_repo.get_actors()
    assert (actors[-1].actor_full_name != actor) == True


def test_repository_can_add_director_and_get_directors_stored_in_repository(in_memory_repo):
    director = Director('Joey Law')
    in_memory_repo.add_director(director)
    directors = in_memory_repo.get_directors()
    assert (director in directors) == True


def test_repository_does_not_add_director_if_parameter_is_not_director_type(in_memory_repo):
    director = 'Joey Law'
    in_memory_repo.add_actor(director)
    directors = in_memory_repo.get_directors()
    assert (directors[-1].director_full_name != director) == True


def test_repository_can_add_genre_and_get_genres_stored_in_repository(in_memory_repo):
    genre = Genre('Crazy')
    in_memory_repo.add_genre(genre)
    genres = in_memory_repo.get_genres()
    assert (genre in genres) == True


def test_repository_does_not_add_genre_if_parameter_is_not_genre_type(in_memory_repo):
    genre = 'Crazy'
    in_memory_repo.add_genre(genre)
    genres = in_memory_repo.get_genres()
    assert (genres[-1].genre_name != genre) == True


def test_repository_can_add_review_and_get_reviews(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    movie = in_memory_repo.get_movie(320)
    review = Review(in_memory_repo.get_movie(320), 'It is very exciting', 6)
    review.user = user
    review.user.add_review(review)
    movie.add_review(review)
    in_memory_repo.add_review(review)
    reviews = in_memory_repo.get_reviews()
    assert (review in reviews) == True
