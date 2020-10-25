class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()
        self._tagged_movies = []

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other.__genre_name:
            return True
        return False

    def __lt__(self, other):
        if self.__genre_name < other.__genre_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__genre_name)

    @property
    def tagged_movies(self):
        return self._tagged_movies

    @property
    def number_of_tagged_movies(self) -> int:
        return len(self._tagged_movies)

    def is_applied_to(self, movie) -> bool:
        return movie in self._tagged_movies

    def add_movie(self, movie):
        self._tagged_movies.append(movie)
