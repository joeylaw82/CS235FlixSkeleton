class Actor:
    def __init__(self, actor_full_name: str):
        self._tagged_movies = []
        self.colleagueList = []
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.__actor_full_name:
            return True
        return False

    def __lt__(self, other):
        if self.__actor_full_name < other.__actor_full_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.colleagueList.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        for i in range(len(self.colleagueList)):
            if self.colleagueList[i] == colleague:
                return True
        return False

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
