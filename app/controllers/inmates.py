from flask import Blueprint, render_template
from ..models.inmates_model import get_lists, get_detail, get_document

bp = Blueprint("inmates", __name__, url_prefix="/inmates")
segment = "inmates"

@bp.route("/", methods=["GET"])
def list_inmates():
    datas = get_lists()
    return render_template("inmates/index.html", data=[segment, datas["items"]])


@bp.route("/detail/<string:uid>", methods=["GET"])
def detail_inmates(uid):
    datas = get_detail(uid)
    docs = get_document(uid)
    return render_template("inmates/detail.html", data=[segment, datas, docs['items']])

@bp.route("/create", methods=["GET"])
def create_inmates():
    return render_template("inmates/create.html", data=[segment])

@bp.route("/update/<string:uid>", methods=["GET"])
def update_inmates(uid):
    datas = get_detail(uid)
    return render_template("inmates/update.html", data=[segment, datas])

@bp.route("/dokumen/<string:uid>", methods=["GET"])
def create_inmates_document(uid):
    datas = get_detail(uid)
    return render_template("inmates/document.html", data=[segment, datas])

@bp.route("/capture/<string:uid>", methods=["GET"])
def capture_inmates_face(uid):
    datas = get_detail(uid)
    return render_template("inmates/capture.html", data=[segment, datas])