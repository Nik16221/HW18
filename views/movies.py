from flask import request
from flask_restx import Resource, Namespace
from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        """
        Выгружаем из базы все фильмы
        """
        data = movie_service.get_movies()

        if len(request.args) > 0:
            # Все отфильтрованные фильмы (1 или более фильтров)
            return movies_schema.dump(movie_service.get_movie_by_many_filter(**request.args))
        else:
            # Все фильмы
            return movies_schema.dump(data), 200

    def post(self):
        """
        Добавляем фильм в базу
        """
        movie_service.add_movie(request.json)
        return "Фильм добавлен!", 201


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):

    def get(self, movie_id):
        """
        Выгружаем из базы фильм по id
        """
        data = movie_service.get_movie_by_id(movie_id)
        return movie_schema.dump(data), 200

    def put(self, movie_id):
        """
        Изменяем данные о фильме по ID
        """
        movie_service.update_movie(request.json)
        return "Информация о фильме обновлена!", 201

    def delete(self, movie_id):
        """
        Удаление фильма из базы по ID
        """
        movie_service.delete_movie(movie_id)
        return "Информация о фильме удалена!", 201
