from flask import Blueprint, render_template

from ..models.attendances_model import get_lists, get_detail

bp = Blueprint("attendances", __name__, url_prefix="/attendances")
segment_masuk = "masuk"
segment_pulang = "pulang"


@bp.route("/masuk", methods=["GET"])
def attendance_masuk():
    datas = get_lists()
    return render_template("attendances/masuk.html", data=[segment_masuk, datas["items"]])

@bp.route("/pulang", methods=["GET"])
def attendance_pulang():
    datas = get_lists()
    return render_template("attendances/pulang.html", data=[segment_pulang, datas["items"]])