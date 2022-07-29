class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db' # путь до бд
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2} #отображение русского текста
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
