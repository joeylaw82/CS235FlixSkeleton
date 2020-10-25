import abc
from typing import List
from datetime import date

from domainmodel.user import User
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre



repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self):
        """ Returns all users stored in the repository
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds a Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, index: int) -> Movie:
        """ Returns Movie with index from the repository.

        If there is no Movie with the given index, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first Movie, ordered by rank, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the last Movie, ordered by rank, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_actor(self, actor_name: str):
        """ Returns a list of Movies that has the Actor.

        If there are no Movie has the Actor, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_actor_list(self, actor_list):
        """ Returns a list of Movies that has the Actors.

        If there are no Movie has the Actors, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_director(self, director_name: str):
        """ Returns a list of Movies that is directed by the Director.

        If there are no Movie direct by this Director, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_genre(self, genre_string: str):
        """ Returns a list of Movies that is has the Genre.

        If there are no Movie has the Genre, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_genre_list(self, genre_list):
        """ Returns a list of Movies that has the genres.

        If there are no Movie has the genres, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_title(self, title: str):
        """ Returns a list of Movies that consist the title the user type in.

        If there are no Movie has the title, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_release_year(self, year: int):
        """ Returns a list of Movies that are release at the year the user type in.

        If there are no Movie release in that year, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """ Adds a Actor to the repository. if actor is not Actor type the repository will not update"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Actor]:
        """ Returns the Actors stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """ Adds a Director to the repository. if director is not Director type the repository will not update"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        """ Returns the Directors stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository. if genre is not Gnre tyoe the repository will not update"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the Genres stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Review to the repository.

        If the Review doesn't have bidirectional links with a Movie and a User, this method raises a
        RepositoryException and doesn't update the repository.
            """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Review not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Review not correctly attached to a Movie')

    @abc.abstractmethod
    def get_reviews(self):
        """ Returns the Reviews stored in the repository. """
        raise NotImplementedError
