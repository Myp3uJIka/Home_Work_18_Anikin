# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

# from flask import Flask
# from flask_restx import Api
#
# from config import Config
# from models import Review, Book
# from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
# def create_app(config_object):
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     register_extensions(app)
#     return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
# def register_extensions(app):
#     db.init_app(app)
#     api = Api(app)
#     api.add_namespace(...)
#     create_data(app, db)
#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)
from flask.app import Flask
from flask_restx.api import Api

from app.config import Config
from app.database import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run()


