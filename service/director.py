from dao.director import DirectorDAO
from dao.model.models import Director


class DirectorService:
    # Через методы класса DAO выводим нужные данные (реализуем логику)
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> list[Director]:
        return self.director_dao.get_all_directors()

    def get_directors_by_id(self, director_id):
        return self.director_dao.get_director_by_id(director_id)
