from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:
    # Через методы класса DAO выводим нужные данные (реализуем логику)
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:  # получаем все фильмы
        return self.movie_dao.get_all_movies()

    def get_movie_by_id(self, movie_id):  # получаем фильм по ID
        return self.movie_dao.get_movie_by_id(movie_id)

    def get_movie_by_many_filter(self, **kwargs):  # получаем все фильм с использованием фильтров
        return self.movie_dao.get_movies_by_many_filters(**kwargs)

    def add_movie(self, data):  # добавляем фильм в бд
        self.movie_dao.create_movie(**data)

    def update_movie(self, data):  # редактируем фильм
        self.movie_dao.update_movie(**data)

    def delete_movie(self, movie_id):  # удаляем фильм
        self.movie_dao.delete_movie(movie_id)
