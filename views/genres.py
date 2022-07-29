from flask_restx import Namespace, Resource

from dao.model.schema import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """
        выгружаем из базы все жанры
        """
        data = genre_service.get_genres()
        return genres_schema.dump(data), 200


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):

    def get(self, genre_id):
        """
        выгружаем из базы жанр по id
        """
        data = genre_service.get_genre_by_id(genre_id)
        return genre_schema.dump(data), 200

