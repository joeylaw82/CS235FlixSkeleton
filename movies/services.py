from typing import List, Iterable

from adapters.repository import AbstractRepository
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.genre import Genre


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_review(movie_id: int, review_text: str, username: str, rating: int, repo: AbstractRepository):
    # Check that the movie exists.
    movie = repo.get_movie(movie_id)
    if movie is None:
        raise NonExistentArticleException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create review.
    review = Review(movie, review_text, rating)
    review.user = user
    review.user.add_review(review)
    movie.add_review(review)

    # Update the repository.
    repo.add_review(review)


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentArticleException

    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):

    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()

    return movie_to_dict(movie)


def get_movie_by_genre(genre_name, repo: AbstractRepository):
    movies = repo.get_movie_by_genre(genre_name)
    movies_as_dict = movies_to_dict(movies)

    return movies_as_dict


def get_movie_by_id(id_list, repo: AbstractRepository):
    movie_list = []
    for id in id_list:
        movie = repo.get_movie(id)
        movie_list.append(movie)

    movies_as_dict = movies_to_dict(movie_list)

    return movies_as_dict


def get_reviews_for_movie(movie_id, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentArticleException

    return reviews_to_dict(movie.reviews)


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'id': movie.rank,
        'title': movie.title,
        'release_year': movie.release_year,
        'description': movie.description,
        'reviews': reviews_to_dict(movie.reviews),
        'genres': genres_to_dict(movie.genres)
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def review_to_dict(review: Review):
    review_dict = {
        'username': review.user.user_name,
        'article_id': review.movie.rank,
        'comment_text': review.review_text,
        'timestamp': review.timestamp
    }
    return review_dict


def reviews_to_dict(reviews: Iterable[Review]):
    return [review_to_dict(review) for review in reviews]


def genre_to_dict(genre: Genre):
    genre_dict = {
        'name': genre.genre_name,
        'tagged_articles': [movie.rank for movie in genre.tagged_movies]
    }
    return genre


def genres_to_dict(genres: Iterable[Genre]):
    return [genre_to_dict(genre) for genre in genres]


# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_article(dict):
    movie = Movie(dict.title, dict.release_year)
    # Note there's no comments or tags.
    return movie
