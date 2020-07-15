from flask import Flask
from ecoleta.ext import (
    site,
    config,
    api,
    db,
    )

def create_app():
    app = Flask(__name__, static_url_path="")

    config.init_app(app)
    db.init_app(app)
    site.init_app(app)
    api.init_app(app)
    
    return app