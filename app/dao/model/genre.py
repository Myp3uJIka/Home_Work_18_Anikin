from marshmallow import fields
from marshmallow.schema import Schema

from app.database import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
