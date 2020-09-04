from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchList = []

    def add_movie(self, movie):
        if type(movie) is Movie and movie not in self.__watchList:
            self.__watchList.append(movie)

    def remove_movie(self, movie):
        if type(movie) is Movie and movie in self.__watchList:
            self.__watchList.remove(movie)

    def size(self):
        return len(self.__watchList)

    def first_movie_in_watchlist(self):
        return self.__watchList[0]

    def select_movie_to_watch(self, index):
        if index >= len(self.__watchList):
            return None
        else:
            return self.__watchList[index]

    def __iter__(self):
        return iter(self.__watchList)

    def __next__(self):
        return next(self.__watchList)



