from flask.globals import request
from flask_restx.namespace import Namespace
from flask_restx.resource import Resource

from app.container import movie_service
from app.dao.model.movie import MovieSchema, FilterSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filtered_data = FilterSchema().load(request.args)
        all_movies = movie_service.get_all(filtered_data)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        movie_service.update(mid, req_json)
        return '', 201

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
