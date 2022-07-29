from flask_restx import Namespace, Resource
from dao.model.schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """
        выгружаем из базы всех режессеров
        """
        data = director_service.get_directors()
        return directors_schema.dump(data), 200


@director_ns.route('/<int:director_id>')
class DirectorsView(Resource):

    def get(self, director_id):
        """
        выгружаем из базы режессера по id
        """
        data = director_service.get_directors_by_id(director_id)
        return director_schema.dump(data), 200
