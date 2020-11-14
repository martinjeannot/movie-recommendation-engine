class Movie:

    def __init__(self, movie):
        self.title, self.year = self.parse_title(movie.title)
        self.index = movie.Index
        self.id = movie.movieId
        self.genres = movie.genres.split('|')

    def parse_title(self, title):
        year = title[-5:-1]
        title = title[:-7]
        if title[-5:] == ', The':
            title = 'The ' + title[:-5]
        return title, year


class Recommendation(Movie):

    def __init__(self, movie, predicted_rating):
        super().__init__(movie)
        self.predicted_rating = predicted_rating
