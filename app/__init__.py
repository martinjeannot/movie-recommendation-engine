from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__, static_folder='./frontend/dist', static_url_path='/', instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # routing
    from app.api.movies import movies
    app.register_blueprint(movies)

    return app


# see https://github.com/benoitc/gunicorn/issues/2159
my_app = create_app()
