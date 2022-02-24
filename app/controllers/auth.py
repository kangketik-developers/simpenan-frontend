from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint("auth", __name__)


@bp.route("/", methods=("GET", "POST"))
def index():
    return render_template("auth/login.html")
