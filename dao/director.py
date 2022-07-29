from dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    # получение нужных данных из базы
    def get_all_directors(self):  # Вызов всех режессеров
        return self.session.query(Director).all()

    def get_director_by_id(self, director_id):  # Вызов режессера по ID
        return self.session.query(Director).filter(Director.id == director_id).one()
