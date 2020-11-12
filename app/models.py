class Movie:

    def __init__(self, movie):
        self.title, self.year = self.parse_title(movie.title)

    def parse_title(self, title):
        year = title[-5:-1]
        title = title[:-7]
        if title[-5:] == ', The':
            title = 'The ' + title[:-5]
        return title, year
