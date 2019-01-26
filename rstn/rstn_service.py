from getrstn import GetRSTN

from flask import Blueprint, Response, request, jsonify

from utils import check_date

rstn_page = Blueprint("rstn", __name__)


@rstn_page.route("/", methods=["GET"])
def index():
    data = {"message": "RSTN Data"}
    return jsonify(data)


@rstn_page.route("/get_data", methods=["GET"])
def rstn_data():
    day = request.args["day"]
    month = request.args["month"]
    year = request.args["year"]

    if not check_date(year, month, day):
        msg = {"message": "Impossible date"}
        return jsonify(msg), 400

    path = "data"
    rstn = GetRSTN(day, month, year, path)
    rstn.decompress_file(download=True)
    try:
        rstn_data = rstn.create_dataframe()
        rstn_data.index = rstn_data.index.map(lambda x: str(x))
        # Remove rows with the same index.
        rstn_data = rstn_data[~rstn_data.index.duplicated(keep="first")]
        return Response(rstn_data.to_json(), mimetype="application/json")
    except:
        error = {"message": "Internal error"}
        return jsonify(error), 500
