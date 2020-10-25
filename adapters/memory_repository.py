import csv
import os
import collections
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from adapters.repository import AbstractRepository, RepositoryException
from domainmodel.user import User
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre


class MemoryRepository(AbstractRepository):
    # Movies ordered by rank.

    def __init__(self):
        self._movies: List[Movie] = list()
        self._actors: List[Actor] = list()
        self._genres: List[Genre] = list()
        self._directors: List[Director] = list()
        self._users: List[Actor] = list()
        self._reviews: List[Review] = list()
        self._movie_rank = dict()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        for user in self._users:
            if username.lower() == user.user_name:
                return user
        return None

    def get_users(self):
        return self._users

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movie_rank[movie.rank] = movie

    def get_movie(self, index: int) -> Movie:
        movie = None

        try:
            movie = self._movie_rank[index]
        except KeyError:
            pass  # Ignore exception and return None.

        return movie

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movie_rank[1]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movie_rank[1000]
        return movie

    def get_movie_by_actor(self, actor_name: str):

        for actor in self._actors:
            if actor.actor_full_name.lower() == actor_name.lower():
                return actor.tagged_movies
        return []

    def get_movie_by_actor_list(self, actor_list):
        result = []
        for actor in self._actors:
            if actor.actor_full_name.lower() in actor_list:
                for movie in actor.tagged_movies:
                    result.append(movie)
        result = [movie for movie, count in collections.Counter(result).items() if count > 1]
        return result

    def get_movie_by_director(self, director_name: str):
        for director in self._directors:
            if director.director_full_name.lower() == director_name.lower():
                return director.tagged_movies
        return []

    def get_movie_by_genre(self, genre_string: str):
        for genre in self._genres:
            if genre.genre_name.lower() == genre_string.lower():
                return genre.tagged_movies
        return []

    def get_movie_by_genre_list(self, genre_list):
        result = []
        for genre in self._genres:
            if genre.genre_name.lower() in genre_list:
                for movie in genre.tagged_movies:
                    result.append(movie)
        result = [movie for movie, count in collections.Counter(result).items() if count > 1]
        return result

    def get_movie_by_title(self, title: str):
        match_movies = []
        for movie in self._movies:
            if movie.title == title.lower() or title.lower() in movie.title.lower():
                match_movies.append(movie)
        return match_movies

    def get_movie_by_release_year(self, year: int):
        match_movies = []
        for movie in self._movies:
            if movie.release_year == year:
                match_movies.append(movie)
        return match_movies

    def add_actor(self, actor: Actor):
        if type(actor) != Actor:
            return
        self._actors.append(actor)

    def get_actors(self) -> List[Actor]:
        return self._actors

    def add_director(self, director: Director):
        if type(director) != Director:
            return
        self._directors.append(director)

    def get_directors(self) -> List[Director]:
        return self._directors

    def add_genre(self, genre: Genre):
        if type(genre) != Genre:
            return
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self._genres

    def add_review(self, review: Review):
        super().add_review(review)
        self._reviews.append(review)

    def get_reviews(self):
        return self._reviews


def read_csv_file(filename: str):
    with open(filename) as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies_and_actors_genres_director(data_path: str, repo: MemoryRepository):
    actor_dict = dict()
    genre_dict = dict()
    directors = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
        movie_key = int(data_row[0])
        genres = data_row[2]
        actors = data_row[5]
        director = data_row[4]
        genre_list = genres.rsplit(",")
        actor_list = actors.rsplit(",")

        for genre in genre_list:
            if genre not in genre_dict.keys():
                genre_dict[genre] = list()
            genre_dict[genre].append(movie_key)

        for actor in actor_list:
            if actor not in actor_dict.keys():
                actor_dict[actor] = list()
            actor_dict[actor].append(movie_key)

        if director not in directors.keys():
            directors[director] = list()
        directors[director].append(movie_key)

        movie = Movie(data_row[1], int(data_row[6]))
        movie.rank = movie_key
        movie.description = data_row[3]
        movie.runtime_minutes = int(data_row[7])
        if data_row[8] != "N/A":
            movie.rating = float(data_row[8])
        if data_row[9] != "N/A":
            movie.votes = int(data_row[9])
        if data_row[10] != "N/A":
            movie.revenue = float(data_row[10])
        if data_row[11] != "N/A":
            movie.metascore = float(data_row[11])

        repo.add_movie(movie)

    for genre_name in genre_dict.keys():
        genre = Genre(genre_name)
        for movie_id in genre_dict[genre_name]:
            movie = repo.get_movie(movie_id)
            genre.add_movie(movie)
            movie.add_genre(genre)
        repo.add_genre(genre)

    for actor_name in actor_dict.keys():
        actor = Actor(actor_name)
        for movie_id in actor_dict[actor_name]:
            movie = repo.get_movie(movie_id)
            actor.add_movie(movie)
            movie.add_actor(actor)
        repo.add_actor(actor)

    for director_name in directors.keys():
        director = Director(director_name)
        for movie_id in directors[director_name]:
            movie = repo.get_movie(movie_id)
            director.add_movie(movie)
            movie.director = director
        repo.add_director(director)


def load_reviews(data_path: str, repo: MemoryRepository, users):
    for data_row in read_csv_file(os.path.join(data_path, 'reviews.csv')):
        movie = repo.get_movie(int(data_row[2]))
        review = Review(movie, data_row[3], int(data_row[4]))
        review.user = users[data_row[1]]
        review.user.add_review(review)
        movie.add_review(review)
        repo.add_review(review)


def load_users(data_path, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            username=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def populate(data_path: str, repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_movies_and_actors_genres_director(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load comments into the repository.
    load_reviews(data_path, repo, users)
