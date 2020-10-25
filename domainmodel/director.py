class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()
        self._tagged_movies = []

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__director_full_name < other.__director_full_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__director_full_name)

    @property
    def tagged_movies(self):
        return self._tagged_movies

    def is_applied_to(self, movie) -> bool:
        return movie in self._tagged_movies

    def add_movie(self, movie):
        self._tagged_movies.append(movie)
