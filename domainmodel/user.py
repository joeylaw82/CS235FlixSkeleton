from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, username, password):
        if username == "" or type(username) is not str:
            self.__user_name = None
        else:
            self.__user_name = username.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, x):
        if x > 0 and type(x) is int:
            self.__time_spent_watching_movies_minutes = x

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self,other):
        if self.__user_name == other.user_name:
            return True
        return False

    def __lt__(self,other):
        if self.__user_name < other.user_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__user_name) + hash(self.__password)

    def watch_movie(self, movie):
        if type(movie) is Movie:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review:
            self.__reviews.append(review)

