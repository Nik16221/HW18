from marshmallow import Schema, fields


# Создание схем
class GenreSchema(Schema):
    __tablename__ = "genre"
    id = fields.Int()
    name = fields.Str()


class DirectorSchema(Schema):
    __tablename__ = "director"
    id = fields.Int()
    name = fields.Str()


class MovieSchema(Schema):
    __tablename__ = "movie"
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Nested(GenreSchema)  # +связанный вложенный список
    director = fields.Nested(DirectorSchema)  # +связанный вложенный список