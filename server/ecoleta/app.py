from flask import Flask
from ecoleta.ext import site

def create_app():
    app = Flask(__name__, static_url_path="")

    site.init_app(app)

    return app