from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title: str, release_year: int):
        self.__actors = []
        self.__genres = []
        self.__director = None
        self.__runtime_minutes = 0
        self.__description = None
        self.__rating = 0.0
        self.__votes = 0.0
        self.__revenue = 0.0
        self.__metascore = 0.0
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year < 1900 or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if new_title == "" or type(new_title) is not str:
            self.__title = None
        else:
            self.__title = new_title.strip()

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actor_list):
        if type(actor_list) is list:
            self.__actors = actor_list

    def add_actor(self, actor):
        if type(actor) is Actor and actor not in self.__actors:
            self.__actors.append(actor)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new):
        if new == "" or type(new) is not str:
            self.__description = None
        else:
            self.__description = new.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, new_director):
        if type(new_director) is not Director:
            self.__director = None
        else:
            self.__director = new_director

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genre_list):
        if type(genre_list) is list:
            self.__genres = genre_list

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.__genres:
            self.__genres.append(genre)

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, x):
        if type(x) is not int or x <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = x

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, x):
        if x < 0 or type(x) is not float:
            raise ValueError
        else:
            self.__rating = x

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, x):
        if type(x) is not int:
            raise ValueError
        else:
            self.__votes = x

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, x):
        if x == 'N/A':
            self.__revenue = x
        else:
            self.__revenue = float(x)

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, y):
        if y == 'N/A':
            self.__metascore = y
        else:
            self.__metascore = int(y)

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if self.__title == other.title and self.__release_year == other.__release_year:
            return True
        return False

    def __lt__(self, other):
        if self.__title == other.title:
            if self.__release_year < other.__release_year:
                return True
            if self.__release_year > other.__release_year:
                return False
        if self.__title < other.__title:
            return True
        return False

    def __hash__(self):
        return hash(self.__title) + hash(self.__release_year)

    def remove_actor(self, actor):
        if type(actor) is Actor and actor in self.__actors:
            self.__actors.remove(actor)

    def remove_genre(self, genre):
        if type(genre) is Genre and genre in self.__genres:
            self.__genres.remove(genre)


