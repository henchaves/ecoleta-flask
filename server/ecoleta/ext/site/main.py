from flask import Blueprint, render_template

bp = Blueprint("site", __name__)

@bp.route("/api")
def index():
    return render_template("api.html")