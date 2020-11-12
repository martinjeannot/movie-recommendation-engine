from flask import Blueprint

movies = Blueprint('movies', __name__, url_prefix='/api/movies')
