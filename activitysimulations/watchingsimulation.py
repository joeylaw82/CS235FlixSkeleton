from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review


class MovieWatchingSimulation:
    def __init__(self, user_list, movie):
        self.__user_list = []
        if type(movie) is Movie:
            self.__movie_watching = movie
        for user in user_list:
            if type(user) is User:
                self.__user_list.append(user)
        self.__review = None

    def __repr__(self):
        return f"Movie watching : {self.__movie_watching}\nUser(s) watching : {self.__user_list}\nReview : {self.__review}"

    @property
    def movie_watch(self):
        return self.__movie_watching

    @property
    def user_list(self):
        return self.__user_list

    @property
    def review(self):
        return self.__review

    def add_review(self, review_text, rating):
        self.__review = Review(self.__movie_watching, review_text, rating)
