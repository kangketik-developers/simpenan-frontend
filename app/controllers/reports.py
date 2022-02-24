from flask import Blueprint, render_template, request

from ..models.reports_model import get_lists, get_lists_filtered

bp = Blueprint("reports", __name__, url_prefix="/reports")
segment = ["penilaian"]


@bp.route("/penilaian", methods=["GET"])
def laporan_penilaian():
    bulan = request.args.get("bulan")
    tahun = request.args.get("tahun")
    if bulan and tahun:
        datas = get_lists_filtered(bulan, tahun)
    else:
        datas = {"items": ""}
    return render_template("reports/penilaian.html", data=[segment[0], datas["items"]])