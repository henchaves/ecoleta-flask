def init_app(app):
    app.config["SECRET_KEY"] = "henrique"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecoleta.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False