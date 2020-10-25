from typing import Iterable
import random

from adapters.repository import AbstractRepository
from domainmodel.movie import Movie


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre_name for genre in genres]

    return genre_names


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()
    movies = []

    if quantity >= movie_count:
        quantity = movie_count - 1

    random_ids = random.sample(range(1, movie_count), quantity)
    for id in random_ids:
        movie = repo.get_movie(id)
        movies.append(movie)

    return movies_to_dict(movies)


# ============================================
# Functions to convert dicts to model entities
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
        'release_year': movie.release_year,
        'rating': movie.rating,
        'votes': movie.votes,
        'metascore': movie.metascore
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]
