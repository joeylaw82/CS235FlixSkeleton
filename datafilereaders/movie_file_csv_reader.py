import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                genres = row['Genre']
                description = row['Description']
                director = row['Director']
                actors = row['Actors']
                runtime = int(row['Runtime (Minutes)'])
                rating = float(row['Rating'])
                votes = int(row['Votes'])
                rev = row['Revenue (Millions)']
                metascore = row['Metascore']
                genre_list = genres.rsplit(",")
                actor_list = actors.rsplit(",")
                movie = Movie(title, release_year)
                movie.runtime_minutes = runtime
                movie.director = Director(director)
                movie.rating = rating
                movie.votes = votes
                movie.revenue = rev
                movie.metascore = metascore
                if movie.director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(movie.director)
                movie.description = description
                if movie not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(movie)
                for genre in genre_list:
                    tmp = Genre(genre)
                    if tmp not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(tmp)
                    movie.add_genre(tmp)
                for actor in actor_list:
                    tmp = Actor(actor)
                    if tmp not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(tmp)
                    movie.add_actor(tmp)
                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

#Checking for alll information linked
filename = '../datafiles/Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()
movie = movie_file_reader.dataset_of_movies[0]
print(movie)
print(movie.director)
print(movie.actors)
print(movie.genres)
print(f"Runtime: {movie.runtime_minutes}")
print(movie.description)
print(f"Rating: {movie.rating}")
print(f"Rating votes: {movie.votes}")
print(f"MetaScore:{movie.metascore}")
print(f"Rev: {movie.revenue}")
