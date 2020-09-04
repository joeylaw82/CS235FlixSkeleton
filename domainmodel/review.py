from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie, review_text, rating):
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
        if 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now().timestamp()

    def __repr__(self):
        return f"{self.__movie}\nReview: {self.__review_text}\nRating: {self.__rating} "

    def __eq__(self, other):
        if type(other) is Review:
            if self.__movie == other.movie and self.__review_text == other.review_text and self.__rating == other.rating and self.__timestamp == other.timestamp:
                return True
        return False

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp


