from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, data):
        return self.dao.get_all(data)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, data):
        movie = self.get_one(mid)
        if 'title' in data:
            movie.title = data['title']
        if 'description' in data:
            movie.description = data['description']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'year' in data:
            movie.year = data['year']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'director_id' in data:
            movie.director_id = data['director_id']
        return self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)

