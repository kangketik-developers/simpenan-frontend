from flask import Blueprint, render_template

from ..models.users_model import get_lists, get_detail

bp = Blueprint("users", __name__, url_prefix="/users")
segment = "users"


@bp.route("/", methods=["GET"])
def list_user():
    datas = get_lists()
    return render_template("users/index.html", data=[segment, datas["items"]])


@bp.route("/detail/<string:uid>", methods=["GET"])
def update_user(uid):
    datas = get_detail(uid)
    return render_template("users/update.html", data=[segment, datas])

@bp.route("/create", methods=["GET"])
def create_user():
    return render_template("users/create.html", data=[segment])